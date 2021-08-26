import json

import requests

from src.sdk.auth.auth_sdk import login
from src.utils.header_utils import build_headers


def import_topics(site,topics):
    headers = build_headers(login(site))
    for topic in topics:
        # print(topic["name"])
        response = requests.post(site["host"] + "import/admin/topic", data=json.dumps(topic),
                                 headers=headers)
        if response.status_code==200:
            print("import successfully")


def import_pipelines(site,pipelines):
    headers = build_headers(login(site))
    for pipeline in pipelines:
        response = requests.post(site["host"] + "import/admin/pipeline", data=json.dumps(pipeline),
                                 headers=headers)
        if response.status_code == 200:
            print("import successfully")


def import_users(site,user):
    headers = {"Content-Type": "application/json"}
    user_site = site.copy()
    user_site["username"]="imma-super"
    headers = build_headers(login(user_site))
    # for user in users:
    response = requests.post(site["host"] + "user", data=json.dumps(user),
                                 headers=headers)

    if response.status_code == 200:
        print("import successfully")


def get_topic_definition_list(site):
    headers = build_headers(login(site))
    response = requests.get(site["host"] + "topic/all"
                            , headers=headers)
    return  response.json()




