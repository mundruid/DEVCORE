import json
import requests

from intersight_auth import IntersightAuth

AUTH = IntersightAuth(
    './.SecretKey.txt',
    api_key_id='60aaa1c67564612d33ceea4e/60aaa1c67564612d33ceea53/60d2609d7564612d305a2361'
)

URL = 'https://intersight.com/api/v1/'

# intersight operations, GET, POST, PATCH, DELETE
OPERATIONS = [
    {
        "request_process": True,
        "resource_path": "compute/PhysicalSummaries",
        "request_method": "GET"
    },
    {
        "request_process": False,
        "resource_path": "ntp/Policies",
        "request_method": "GET"
    },
    {
        "request_process": False,
        "resource_path": "ntp/Policies",
        "request_method": "POST",
        "request_body": {
            "Enabled": True,
            "Name": "ntp-policy",
            "Description": "NTP Policy for ntp.org",
            "NtpServers": [
                "pool.ntp.org"
            ],
            "Tags":[]
        }
    },
    {
        "request_process": False,
        "resource_path": "ntp/Policies",
        "request_method": "POST",
        "request_body": {
            "Enabled": True,
            "Name": "ntp-policy-west",
            "Description": "NTP Policy for ntp.org West Coast",
            "NtpServers": [
                "0.pool.ntp.org",
                "1.pool.ntp.org"
            ],
            "Tags":[]
        }
    },
    {
        "request_process": False,
        "resource_path": "ntp/Policies",
        "request_method": "POST",
        "request_body": {
            "Enabled": True,
            "Name": "ntp-policy-east",
            "Description": "NTP Policy for ntp.org East Coast",
            "NtpServers": [
                "2.pool.ntp.org",
                "3.pool.ntp.org"
            ],
            "Tags":[]
        }
    },
    {
        "request_process": False,
        "resource_name": "ntp-policy",
        "resource_path": "ntp/Policies",
        "request_method": "PATCH",
        "request_body": {
            "NtpServers": [
                "pool.ntp.org",
                "10.10.10.30"
            ]
        }
    },
    {
        "request_process": False,
        "resource_name": "ntp-policy-east",
        "resource_path": "ntp/Policies",
        "request_method": "DELETE"
    }
]

for operation in OPERATIONS:

    if operation['request_process']:

        response = None
        print(operation['request_method'])

        # GET
        if operation['request_method'] == "GET":
            response = requests.get(
                URL + operation['resource_path'],
                auth=AUTH
            )

        # POST
        if operation['request_method'] == "POST":
            response = requests.post(
                URL + operation['resource_path'],
                data=json.dumps(operation['request_body']),
                auth=AUTH
            )

        # PATCH
        if operation['request_method'] == "PATCH":

            # GET the Moid of the MO to PATCH
            response = requests.get(
                (
                    URL + operation['resource_path'] +
                    "?$filter=Name eq '" + operation['resource_name'] + "'"
                ),
                auth=AUTH
            )

            # Extract the Moid from the Results
            json_result = json.loads(response.text)
            moid = json_result["Results"][0]["Moid"]

            response = requests.patch(
                URL + operation['resource_path'] + "/" + moid,
                data=json.dumps(operation['request_body']),
                auth=AUTH
            )

        # DELETE
        if operation['request_method'] == "DELETE":

            # GET the Moid of the MO to DELETE
            response = requests.get(
                (
                    URL + operation['resource_path'] +
                    "?$filter=Name eq '" + operation['resource_name'] + "'"
                ),
                auth=AUTH
            )

            # Extract the Moid from the Results
            json_result = json.loads(response.text)
            moid = json_result["Results"][0]["Moid"]

            response = requests.delete(
                URL + operation['resource_path'] + "/" + moid,
                auth=AUTH
            )

        print(response.status_code)
        print(response.text)
