import requests
import time

from datetime import datetime

ATTEMPTS = 10000
url = "https://httpbin.org/get"

current_time = datetime.now()
for i in range(ATTEMPTS):
    try:
        resp = requests.get(url=url, timeout=0.2)
    # if resp.status_code == 429:
    except:
        duration = datetime.now() - current_time
        limiting_attempts = i
        print(f"Rate limited after {i} attempts in {duration} time")
        break

for i in range(100):
    resp = requests.get(url=url, timeout=0.25)
    if ((i+1) % limiting_attempts) == 0:
        time.sleep(1)
