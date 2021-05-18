import os

from helpers import find_network, req


def main():
    """Workflow to get ssid"""
    print("starting meraki workflow to get ssid")
    env = os.environ.get
    TOKEN = env("MERAKI_TOKEN", "")

    org_name = "DeLab"
    net_name = "Lyoli"

    # find the network
    net_id = find_network(org_name, net_name, TOKEN)

    # print network and find ssid
    ssids = req(f"networks/{net_id}/ssids", "get", TOKEN).json()

    for ssid in ssids:
        print(f"Num: {ssid['number']} Enabled: {ssid['enabled']}")
        print(f"Name: {ssid['name']}")


if __name__ == "__main__":
    main()
