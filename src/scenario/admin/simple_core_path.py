from src.sdk.admin.admin_sdk import import_topics, import_spaces, import_pipelines
from src.sdk.common.common_sdk import import_instances, remove_topic_collection, get_value_from_subject
from src.utils.file_utils import load_topics, load_spaces, load_pipelines, load_instances


def __build_header():
    pass


def clean_instance_data():
    remove_topic_collection(["test_raw_data", "test_aggregate_data", "test_distinct_data", "test_array_factor"])

    topic_data_list = []

    ## clean topic data

    pass


def import_metadata():
    ## login with admin user

    import_topics(load_topics())
    import_spaces(load_spaces())
    import_pipelines(load_pipelines())

    ## import user group
    ## import topic

    ## import space
    ## import pipeline


def import_instance_data():
    import_instances(load_instances())


def verify_topic_data():
    query_data = {
        "subjectId": "5630718939369456837",
        "columnName": "aggr",
        "conditions": {
            "jointType": "and",
            "filters": [
                {
                    "columnName": "group",
                    "operator": "equals",
                    "value": "text2"
                }
            ]
        }
    }
    value = get_value_from_subject(query_data)
    data = value[0]
    assert data == '500'


def main():
    clean_instance_data()
    import_metadata()
    import_instance_data()
    import_instance_data()
    verify_topic_data()
    # clean_instance_data()
