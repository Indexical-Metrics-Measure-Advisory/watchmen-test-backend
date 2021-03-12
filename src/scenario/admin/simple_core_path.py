from src.sdk.admin.admin_sdk import import_topics, import_spaces, import_pipelines
from src.sdk.common.common_sdk import import_instances, remove_topic_collection, load_topic_instances
from src.utils.file_utils import load_topics, load_spaces, load_pipelines, load_instances


def clean_instance_data():
    print("cleaning instance data for testing")
    remove_topic_collection(["test_raw_data","test_aggregate_data","test_distinct_data"])


def import_metadata():
    print("importing  metadata for testing ")
    import_topics(load_topics())
    import_spaces(load_spaces())
    import_pipelines(load_pipelines())


def import_instance_data():
    print("importing  instance data ")
    import_instances(load_instances())


def __load_topic_aggregate():
    return load_topic_instances("test_aggregate_data")



def verify_topic_data():

    print("verify data correct")
    results = __load_topic_aggregate()

    data_list = [result["data"] for result in results]
    # print(data_list)
    for data in data_list:
        if data["group_id"]=="text2":
            assert data["sum_number_factor"] ==500
        if data["group_id"]=="text3":
            assert  data["sum_number_factor"] ==400



def main():
    clean_instance_data()
    import_metadata()
    import_instance_data()
    verify_topic_data()
    print("all pass ")
    # clean_instance_data()
