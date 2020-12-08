# auth_token.py
# Get token host 
# raise for status
# return token

import requests
import json
import getpass

def get_token(url, username, password):
    path = "/dna/system/api/v1/auth/token"
    auth = (username, password)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    resp = requests.post(url=f"{url}{path}", headers=headers, auth=auth)

    return resp.json()["Token"]

def main():
    """
    Execution begins here.
    """
    password = getpass.getpass(prompt='Password: ', stream=None)
    # Use the always-on sandbox as a quick test
    token = get_token("https://sandboxdnac2.cisco.com", "devnetuser", password)
    print(token)

if __name__ == "__main__":
    main()
