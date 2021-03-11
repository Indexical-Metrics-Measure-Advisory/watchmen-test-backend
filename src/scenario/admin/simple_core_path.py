from src.sdk.admin.admin_sdk import import_topics, import_spaces, import_pipelines
from src.sdk.common.common_sdk import import_instances, remove_topic_collection
from src.utils.file_utils import load_topics, load_spaces, load_pipelines, load_instances


def clean_instance_data():
    remove_topic_collection(["test_raw_data","test_aggregate_data","test_distinct_data"])


def import_metadata():
    import_topics(load_topics())
    import_spaces(load_spaces())
    import_pipelines(load_pipelines())


def import_instance_data():
    import_instances(load_instances())


def verify_topic_data():


    pass


def main():
    clean_instance_data()
    import_metadata()
    import_instance_data()
    verify_topic_data()
    # clean_instance_data()
