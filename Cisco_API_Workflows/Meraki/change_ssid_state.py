import sys

from helpers import find_network, req

def main(argv):

    # make user enter exactly three arguments
    if len(argv) != 3:
        print(f"usage: python {argv[0]} <ssid#> <0 (off) or 1 (on)>")
        sys.exit(1)

    ssid_number = int(argv[1])
    ssid_enable = bool(argv[2])

    # find network
    org_name = "DeLab"
    net_name = "Lyoli"
    net_id = find_network(org_name, net_name)

    # PUT to update existing ssid by number by changing the enabled state
    payload = {
        "enabled": ssid_enable
    }
    put_ssid = req(f"networks/{net_id}/ssids/{ssid_number}", "put", payload).json()

    # print json of enabled ssid configuration
    print(put_ssid)

if __name__ == "__main__":
    main(sys.argv)
