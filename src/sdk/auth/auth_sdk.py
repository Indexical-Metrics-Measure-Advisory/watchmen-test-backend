import requests


def login():
    login_data = {"username": "imma-admin", "password": "abc1234","grant_type":"password"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post("http://localhost:8000/login/access-token", data=login_data,
                             headers=headers)
    auth_token = response.json()["access_token"]
    # print(auth_token)
    return auth_token

# login()