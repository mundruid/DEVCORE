"""Experiment with httpbin timeout, catch exceptions and eventually get to the site."""
import requests

url = "https://httpbin.org/get"
timeout = 0.001
ATTEMPTS = 5

for i in range(ATTEMPTS):
    try:
        resp = requests.get(url=url, timeout=timeout)
        print(resp.json())
        if resp.ok:
            break
    except requests.exceptions.ConnectTimeout:
        print("Timed out with Connect Timeout!")
        timeout = timeout * 10
    except requests.exceptions.ReadTimeout:
        print("Timed out with Read Timeout!")
        timeout = timeout * 10
