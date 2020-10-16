"""Simple workflow to get token, information about user, and change password """
import requests
import os
import pprint


env = os.environ.get
password = env("UCS_PASSWORD", "")


def get_token(url):
    section = f"opName=getRESTKey&user=admin&password={password}"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    resp = requests.get(url=f"{url}{section}", headers=headers, verify=False)

    return resp.json()


def get_profile(url, token):
    section = "opName=userAPIGetMyLoginProfile"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cloupia-Request-Key": token,
    }

    resp = requests.get(url=f"{url}{section}", headers=headers, verify=False)

    return resp.json()


def change_password(url, token):
    section = "formatType=json&opName=userAPIModifyLoginProfilePassword&opData={param0:{'oldPassword':'old-password', 'newPassword':'new-password'}}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cloupia-Request-Key": token,
    }

    resp = requests.get(url=f"{url}{section}", headers=headers, verify=False)

    return resp.json()


def invoke_custom_task(url, token):
    json_structure = {
        "param0": "InvokeCustTask",
        "param1": {
            "list": [
                {"name": "First Input", "value": "Another"},
                {"name": "Second Input", "value": "User"},
            ]
        },
        "param2": -1,
    }
    section = f"formatType=json&opName=userAPISubmitWorkflowServiceRequest&opData={json_structure}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cloupia-Request-Key": token,
    }

    resp = requests.get(url=f"{url}{section}", headers=headers, verify=False)

    return resp.json()


if __name__ == "__main__":
    url = "https://10.10.20.101/app/api/rest?"

    token = get_token(url)

    profile = get_profile(url, token)
    pprint.pprint(profile)

    change_pass = change_password(url, token)
    pprint.pprint(change_pass)

    invoke_task = invoke_custom_task(url, token)
    pprint.pprint(invoke_task)
