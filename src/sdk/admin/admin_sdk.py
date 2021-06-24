import json

import requests

from src.sdk.auth.auth_sdk import login
from src.utils.header_utils import build_headers


def import_topics(site,topics):
    headers = build_headers(login(site))
    for topic in topics:
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
    # headers = build_headers(login(site))
    headers = {"Content-Type": "application/json"}
    # for user in users:
    response = requests.post(site["host"] + "user", data=json.dumps(user),
                                 headers=headers)
    if response.status_code == 200:
        print("import successfully")