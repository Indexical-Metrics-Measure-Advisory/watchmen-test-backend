import time

import arrow

from src.model.case import TopicData
from src.model.test_result import TestResult, TopicTestResult, FactorNotMatch
from src.sdk.admin.admin_sdk import get_topic_definition_list
from src.sdk.common.common_sdk import import_instances, load_topic_data_all, remove_topic_collection
from src.utils.date_utils import is_date

DATA = "data"


def execute_cases(cases, site, clean):
    case_results = []

    for case in cases:
        case_results.append(execute(case, site, clean))
    return case_results


## TODO __prepared_before_topic_data
def __prepared_before_topic_data(data_before_run, site):
    if data_before_run:
        print("prepare before data")
        for prepare_topic_data in data_before_run:
            topic_name = prepare_topic_data.topic
            data_list = prepare_topic_data.data
            instances = []
            for data in data_list:
                instance = {"code": topic_name, "data": data}
                instances.append(instance)
                import_instances(instances, site)
        print("prepare before data done")
    else:
        print("dataBefore is empty")
        return []


def __trigger_pipeline(trigger_data: TopicData, site):
    data_list = trigger_data.data
    request_list = []
    for data in data_list:
        request_list.append({
            "code": trigger_data.topic,
            "data": data
        })

    results = import_instances(request_list, site)
    return results


def __all_success(results):
    success = True
    for result in results:
        success = result["received"]

    return success


def __get_topic_data(data_after_run, site):
    topic_data_list = {}
    for expected_data in data_after_run:
        topic_data = load_topic_data_all(expected_data.topic, site)
        topic_data_list[expected_data.topic] = topic_data

    return topic_data_list


def find_topic_data(exp_data, topic_data_list):
    key = list(exp_data.keys())[0]
    for topic_data in topic_data_list:
        if topic_data[DATA][key] == exp_data[key]:
            return topic_data[DATA]
    return None


def __find_topic(topic_name, topic_list):
    for topic in topic_list:
        if topic_name == topic["name"]:
            return topic


def build_execute_result(topic_results, case, topic_list):
    test_result = TestResult()
    test_result.caseName = case.caseName
    test_result.rawTopicName = case.triggerData.topic
    for expected_data in case.dataAfterRun:
        topic_result = TopicTestResult()
        topic_name = expected_data.topic
        topic_data_list = topic_results[topic_name]
        topic = __find_topic(topic_name, topic_list)
        topic_result.topicName = topic_name
        topic_result.instanceCount = len(topic_data_list)
        topic_result.expectedCount = len(expected_data.data)
        topic_result.countMatch = topic_result.expectedCount == topic_result.instanceCount
        for index, exp_data in enumerate(expected_data.data):
            if topic["type"] != "raw":
                topic_data = find_topic_data(exp_data, topic_data_list)
                for key, value in exp_data.items():
                    if topic_data is None:
                        topic_data = topic_data_list[index][DATA]
                    topic_value = topic_data[key]
                    if isinstance(topic_value, str) and is_date(topic_value):
                        topic_date = arrow.get(topic_value)
                        date = arrow.get(value)
                        if topic_date != date:
                            factor_not_match = build_factor_not_match(date, key, topic_date)
                            topic_result.factorNotMatchList.append(factor_not_match)
                    else:
                        if value != topic_value:
                            factor_not_match = build_factor_not_match(value, key, topic_value)
                            topic_result.factorNotMatchList.append(factor_not_match)
        test_result.topicResults.append(topic_result)
    return test_result


def build_factor_not_match(date, key, topic_date):
    factor_not_match = FactorNotMatch()
    factor_not_match.factorName = key
    factor_not_match.expectedValue = date
    factor_not_match.value = topic_date
    return factor_not_match


def clear_topic_data(data_after_run, site):
    remove_topic_name_list = []
    for expected_data in data_after_run:
        remove_topic_name_list.append(expected_data.topic)

    remove_topic_collection(remove_topic_name_list, site)


def execute(case, site, clean):
    __prepared_before_topic_data(case.dataBeforeRun, site)
    print("prepared_before_topic_data")
    current_time = time.time()
    results = __trigger_pipeline(case.triggerData, site)
    print(time.time() - current_time)
    if __all_success(results):
        print("__all_success")
        topic_list = get_topic_definition_list(site)
        topic_results = __get_topic_data(case.dataAfterRun, site)
        print("__get_topic_data")
        if clean:
            clear_topic_data(case.dataAfterRun, site)
        # expected_topic_name_list = (list(map(lambda x: x.topic, case.dataAfterRun)))
        print("build_execute_result")
        return build_execute_result(topic_results, case, topic_list)
    else:
        raise Exception("trigger_pipeline error {}".format(results))
