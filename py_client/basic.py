import requests

endpoint = "https://httpbin.org/#/HTTP_Methods/get_get"

get_response = requests.get(endpoint)
print(get_response)