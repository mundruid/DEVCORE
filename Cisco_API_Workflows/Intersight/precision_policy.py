import json
import requests

from intersight_auth import IntersightAuth

AUTH = IntersightAuth(
    './.SecretKey.txt',
    api_key_id='60aaa1c67564612d33ceea4e/60aaa1c67564612d33ceea53/60d2609d7564612d305a2361'
)

URL = 'https://intersight.com/api/v1/'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# Create Server Boot Policy
payload = {
    "Name": "server-boot-from-local-disk-policy",
    "Description": "Boot Server from Local Disk",
    "BootDevices": [
        {
            "ObjectType": "boot.LocalDisk",
            "Enabled": True,
            "Name": "boot"
        },
        {
            "ObjectType": "boot.LocalCdd",
            "Enabled": True,
            "Name": "vmedia"
        }
    ]
}

path = "boot/PrecisionPolicies/"
response = requests.post(url=URL+path, headers=headers,
                         json=payload, auth=AUTH)
moid = response.json()["Moid"]

print(response.text)

# Retrieve Server Boot Policy
response = requests.get(url=URL+path+moid, headers=headers, auth=AUTH)

print(response.text)
