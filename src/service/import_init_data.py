import json

from src.sdk.admin.admin_sdk import import_users, import_topics, import_pipelines
from src.service.load_case import load_topic_list_in_folder, load_pipeline_list_in_folder


def __load_users(site):
    with open("./src/demo_user.json") as f:
        # print(f)
        return json.load(f)

def init_master_data(site, path):
    user = __load_users(site)

    import_users(site, user)
    topics = load_topic_list_in_folder(path)
    import_topics(site, topics)
    pipelines = load_pipeline_list_in_folder(path)
    import_pipelines(site, pipelines)
