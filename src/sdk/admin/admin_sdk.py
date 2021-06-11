import json

import requests

from src.sdk.auth.auth_sdk import login
from src.utils.header_utils import build_headers


def import_topics(topics):
    headers = build_headers(login())
    for topic in topics:
        response = requests.post("http://localhost:8000/import/admin/topic", data=json.dumps(topic),
                                 headers=headers)
        # print(response.status_code)


def import_spaces(spaces):
    headers = build_headers(login())
    for space in spaces:
        response = requests.post("http://localhost:8000/import/admin/space", data=json.dumps(space),
                                 headers=headers)
        print(response.status_code)


def import_pipelines(pipelines):
    headers = build_headers(login())
    for pipeline in pipelines:
        response = requests.post("http://localhost:8000/import/admin/pipeline", data=json.dumps(pipeline),
                                 headers=headers)
        print(response.status_code)
