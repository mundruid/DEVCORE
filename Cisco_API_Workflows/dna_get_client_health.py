# handle API timeouts
# Add timeout & attempts
# loop through attempts
# issue GET with timeout
# try catch
# either terminate after x attempts or not

import requests
import getpass
import time
import json
import pprint

import dna_auth_token 

TIMEOUT = 20
ATTEMPTS = 3

def main():
    url = "https://sandboxdnac2.cisco.com"
    password = getpass.getpass(prompt='Password: ', stream=None)
    token = dna_auth_token.get_token(url, "devnetuser", password)

    headers = {"Content-Type": "application/json", "X-Auth-Token": token}

    current_epoch = int(time.time() * 1000)
    params = {"timestamp": current_epoch}

    for i in range(ATTEMPTS):

        try:
            resp = requests.get(
                f"{url}/dna/intent/api/v1/client-health",
                headers=headers,
                params=params,
                timeout=TIMEOUT
            )

            if resp.ok:
                break
        
        except requests.exceptions.ReadTimeout:
            print(f"Timeout {i+1}/ATTEMPTS ({TIMEOUT} sec)")
            if i+1 == ATTEMPTS:
                print("Could not connect client health")
                import sys
                sys.exit(1)

    # Convert HTTP response body to JSON to extract health data
    get_resp_json = resp.json()
    pprint.pprint(get_resp_json)

    # Print JSON response for troubleshooting and learning
    # import json; print(json.dumps(get_resp_json, indent=2))

    # Iterate over all score details and categories
    # for score in get_resp_json["response"]:
    #     for cat in score["scoreDetail"]:

    #         # Print the client type (wired or wireless) then the quantity
    #         # of clients at each quality level. Finish up with a newline
    #         print(f"{cat['scoreCategory']['value']} client health")
    #         for qual in cat["scoreList"]:
    #             print(f"  {qual['scoreCategory']['value']:<6}", end=" ")
    #             print(f"clients: {qual['clientCount']}")
    #         print()

if __name__ == "__main__":
    main()
