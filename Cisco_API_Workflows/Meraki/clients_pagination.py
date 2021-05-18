import os

from helpers import get_all_networks, get_all_orgs, bluetooth_clients_pagination


def main():
    """Workflow to get clients using pagination"""

    print("starting meraki workflow to get clients")
    env = os.environ.get
    TOKEN = env("MERAKI_TOKEN", "")

    organizations = get_all_orgs(TOKEN)
    for org in organizations.json():
        networks = get_all_networks(org["id"], TOKEN)
        for net in networks.json():
            bluetooth_clients_pagination(net["id"], 10, TOKEN)


if __name__ == "__main__":
    main()
