import requests
import getpass
from requests.compat import urljoin
import pprint
import json


API_URL = "https://10.10.20.65/api/fdm/latest"


def get_token():
    """Get authorization token."""
    requests.packages.urllib3.disable_warnings()
    # URL for getting an access token
    path = f"{API_URL}/fdm/token"
    token_payload = {
        "grant_type": "password",
        "username": "admin",
        "password": getpass.getpass(prompt='Password: ', stream=None)
    }
    # Make the request for an access token using Basic auth/client data
    response = requests.post(path, json=token_payload, verify=False)
    response.raise_for_status()
    return response


def get_network_objects(token):
    """Get network objects."""
    # URL for getting all Firepower objects
    path = f"{API_URL}/object/networks"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    return requests.get(url=path, headers=headers, verify=False)


def add_network_objects(token, object):
    """Create a network object."""
    path = f"{API_URL}/object/networks"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    return requests.post(url=path, headers=headers, json=object, verify=False)


def edit_network_objects(token, url, payload):
    """Create a network object."""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    return requests.put(url=url, headers=headers, json=payload, verify=False)


def delete_network_objects(token, link):
    """Delete a network object."""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    return requests.delete(url=link, headers=headers, verify=False)


if __name__ == "__main__":
    token = get_token().json()["access_token"]
    print(token)
    objects = get_network_objects(token).json()
    pprint.pprint(objects)
    object_names = [obj['name'] for obj in objects['items']]

    # read file with objects
    with open("./objects.json", "r") as file_handle:
        network_objects = json.load(file_handle)

    # add the objects
    for obj in network_objects:
        # idempotency
        if obj['name'] not in object_names:
            add_network_objects(token, obj)
        else:
            # edit if diff
            for item in objects['items']:
                if item['name'] == obj['name']:
                    # compare all keys
                    print(item['name'])
                    k1 = set(item.keys())
                    k2 = set(dict(obj).keys())
                    common_keys = set(k1).intersection(set(k2))
                    for key in common_keys:
                        if item[key] != obj[key]:
                            print(key)
                            print(item[key])
                            edit_network_objects(
                                token, item['links']['self'], item)

    new_objects = get_network_objects(token).json()
    pprint.pprint(objects)

    for obj in new_objects['items']:
        print(obj['links']['self'])
        delete_network_objects(token, obj['links']['self'])
