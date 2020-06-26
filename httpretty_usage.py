import httpretty
import json
import re
import requests

# ---- Part 1 - basic usage

httpretty.enable()

URL = 'https://google.com/'

httpretty.register_uri(httpretty.GET, URL)
response = requests.get(URL)
print(response)
print(response.status_code)

httpretty.disable()
httpretty.reset()


# ---- Part 2 - using with body

httpretty.enable()

URL = 'https://google.com/'

body = "olar"

httpretty.register_uri(httpretty.GET, URL, body=body)
response = requests.get(URL)

print(response)
print(response.status_code)
print(response.content)

httpretty.disable()
httpretty.reset()


# ---- Part 3 - using with json body

httpretty.enable()

URL = 'https://myapi.org/api'

my_json_response = [
    {'a': 1},
    {'b': 2},
    {'c': 3},
]
body = json.dumps(my_json_response)

httpretty.register_uri(httpretty.GET, URL, body=body)
response = requests.get(URL)

print(response.content)
print(response.json())

httpretty.disable()
httpretty.reset()

# ---- Part 4 - using URI with regex
httpretty.enable()

uri = re.compile(r'https://.*')

my_json_response = [
    {'a': 1},
    {'b': 2},
    {'c': 3},
]
body = json.dumps(my_json_response)

httpretty.register_uri(httpretty.GET, uri, body=body)
response = requests.get(URL)

print(response.content)
print(response.json())

httpretty.disable()
httpretty.reset()
