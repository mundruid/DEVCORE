import json
import requests
from requests.models import HTTPError

from intersight_auth import IntersightAuth

AUTH = IntersightAuth(
    './.SecretKey.txt',
    api_key_id='60aaa1c67564612d33ceea4e/60aaa1c67564612d33ceea53/60d2609d7564612d305a2361'
)

URL = 'https://intersight.com/api/v1/'

headers = {
    "Accept": "application/json",
}

# GET VLANS
path = "fabric/Vlans"
try:
    response = requests.get(url=URL+path, auth=AUTH)
except HTTPError as e:
    print(f"HTTP error {e}")
print(response.text)

# get Physical summaries select Dn, top 5
path = "compute/PhysicalSummaries"
# equivalent endpoint if you do not use params
# path = "compute/PhysicalSummaries?$top=5&$select=Model,Dn,Name"
params = {"$top": 5, "$select": "Model,Dn,Name"}
try:
    response = requests.get(url=URL+path, auth=AUTH, params=params)
except HTTPError as e:
    print(f"HTTP error {e}")
print(response.text)
