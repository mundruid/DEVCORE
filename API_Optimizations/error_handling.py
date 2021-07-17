import requests

# code = "400, 401, 403, 404, 409, 429, 500"
code = 401
url = f'https://httpbin.org/status/{code}'
try:
    response = requests.get(url=url)
except requests.exceptions.HTTPError as e:
    print(f"An error {e} occured.")


# response = requests.get(url=url)
# response.raise_for_status()


if response.status_code == 401:
    print("Unauthorized")
elif response.status_code == 403:
    print("Forbidden")
elif response.status_code == 400:
    print("Bad request")
elif response.status_code == 404:
    print("Not found")
elif response.status_code == 429:
    print("too many requests")
elif response.status_code == 500:
    print("internal server error")
elif response.status_code == 505:
    print("HTTP version not supported")
elif response.status_code == 503:
    print("Service unavailable")
elif response.status_code == 502:
    print("Bad gateway")
else:
    print("HTTP error")
