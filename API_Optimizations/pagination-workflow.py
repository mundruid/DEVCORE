"""Pagination experiment with atlassian."""
import os
import requests

from requests.models import HTTPError

env = os.getenv

url = "https://networktocode.atlassian.net/confluence/rest/api"
token = env("ATLASSIAN_TOKEN")
auth = ("xenia.mountrouidou@networktocode.com", token)
# basic get to see if token works

path = "/content/page?limit=5"
contents = []
try:
    response = requests.get(url=url+path, auth=auth)
    contents = response.json()["results"]
    while(response.json()["_list"].get("next")):
        try:
            response = requests.get(
                url=response.json()["_list"]["next"], auth=auth)
            contents.append(response.json()["results"])
        except HTTPError as e:
            print(f"Error {e}")

except HTTPError as e:
    print(f"Error {e}")
