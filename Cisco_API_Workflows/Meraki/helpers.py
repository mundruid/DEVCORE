"""Simple workflow mostly with GET requests to gather information about mobile devices
 using the Cisco Meraki API"""
import requests
import json

# Get basic SSID info

def find_network(org_name, net_name):
    # get list of organizations
    orgs = req("organizations", "get").json()
    print(orgs)

    # iterate list of orgs, find org_id
    for organization in orgs:
        if organization['name'] == org_name:
            org_id = organization['id']

    print(f"Org ID: {org_id}")

    # get all networks in org
    nets = req(f"organizations/{org_id}/networks", "get").json()
    print(nets)

    # iterate over networks, return network id
    for network in nets:
        if network['name'] == net_name:
            net_id = network['id']

    return net_id

def req(resource, method, json=None):
    api_path = "https://dashboard.meraki.com/api/v0/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    resp = requests.request(method=method, url=f"{api_path}/{resource}", headers=headers, json=json)
    resp.raise_for_status()

    return resp
