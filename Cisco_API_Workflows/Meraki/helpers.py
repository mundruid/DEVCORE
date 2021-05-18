"""Simple workflow mostly with GET requests to gather information about mobile devices
 using the Cisco Meraki API"""
import requests
import pprint


def get_all_networks(org_id, token):
    """get all networks for organization with org_id

    Args:
        token ([type]): [description]

    Returns:
        [type]: [description]
    """
    return req(
        f"/organizations/{org_id}/networks",
        "get",
        token
    )


def get_all_orgs(token):
    """get all organizations

    Args:
        token ([type]): [description]

    Returns:
        [type]: [description]
    """
    return req(
        f"organizations",
        "get",
        token
    )


def bluetooth_clients_pagination(network_name, per_page, token):
    """Print network clients using pagination

    Args:
        network_name (str): network name
        per_page (int): objects to display
    """

    clients = req(
        f"networks/{network_name}/bluetoothClients?perPage={per_page}&startingAfter=0",
        "get",
        token
    )

    pprint.pprint(clients.json())


def find_network(org_name, net_name, token):
    # get list of organizations
    orgs = req("organizations", "get", token).json()
    print(orgs)

    # iterate list of orgs, find org_id
    for organization in orgs:
        if organization['name'] == org_name:
            org_id = organization['id']

    print(f"Org ID: {org_id}")

    # get all networks in org
    nets = req(f"organizations/{org_id}/networks", "get", token).json()
    print(nets)

    # iterate over networks, return network id
    for network in nets:
        if network['name'] == net_name:
            net_id = network['id']

    return net_id


def req(resource, method, token, json=None):
    api_path = "https://dashboard.meraki.com/api/v0/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": token
    }

    resp = requests.request(
        method=method, url=f"{api_path}/{resource}", headers=headers, json=json)
    resp.raise_for_status()

    return resp
