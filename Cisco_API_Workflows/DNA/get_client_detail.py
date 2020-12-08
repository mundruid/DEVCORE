# get client detail
# find a way to get the clients mac addresses with the API
# handle rate limiting

import requests
import getpass
import time
import json
import sys
import re
from tqdm import tqdm

import auth_token 

# Cisco DNA allows only 5 reqs per minute
REQS_PER_MINUTE = 5

def main(argv):
    url = "https://sandboxdnac2.cisco.com"
    password = getpass.getpass(prompt='Password: ', stream=None)
    token = auth_token.get_token(url, "devnetuser", password)

    headers = {"Content-Type": "application/json", "X-Auth-Token": token}

    current_epoch = int(time.time() * 1000)
    params = {"timestamp": current_epoch}

    macs = get_macs(argv)

    for i, mac in enumerate(macs):
        params["macAddress"] = mac

        resp = requests.get(
            f"{url}/dna/intent/api/v1/client-detail", 
            headers=headers, 
            params=params
            )
        
        if not resp.ok:
            print(f"Request failed: {resp.status_code}/{resp.reason}")
            print(json.dumps(resp.json(), indent=4))

        stats = resp.json()["detail"]
        print(f"Wireless details for MAC {mac}")
        print(f"  IPv4 Address: {stats['hostIpV4']}")
        print(f"  Freq/chan: {stats['frequency']} GHz / {stats['channel']}")
        print(f"  RSSI/SNR: {stats['rssi']} / {stats['snr']}\n")

        if (i + 1) % REQS_PER_MINUTE == 0:
            print("*** Sleeping for 1 minute to avoid API throttle ***")
            time.sleep(60)


def get_macs(argv):
    """
    Returns a list of valid MAC addresses from the CLI arguments.
    Using regular expression (regex) to validate that input is in the
    proper format, such as "00:00:2A:01:00:01" to give a specific example.
    """

    # Ensure there is at least one MAC specified. If not, print usage and exit
    if len(argv) < 2:
        print(f"usage: python {sys.argv[0]} <mac1> <mac2> ... <macN>")
        sys.exit(1)

    # Create empty list of valid MACs and hex digit regex char pattern
    macs = []
    h2 = "[0-9a-fA-F]{2}"
    regex = re.compile(f"{h2}:{h2}:{h2}:{h2}:{h2}:{h2}")

    # Check each CLI arg for a match against pattern, and add to list
    # using uppercase letters if match succeeds
    for arg in argv[1:]:
        if regex.match(arg):
            macs.append(arg.upper())

    # Return new list of valid MAC addresses
    return macs


if __name__ == "__main__":
    # Ensure main() has access to the system CLI args from the shell
    main(sys.argv)
