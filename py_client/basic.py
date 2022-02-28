import requests

endpoint="https://httpbin.org/status/200/"
endpoint2="https://httpbin.org/anything"

#data is sent as form data, the json data is json data
get_response=requests.get(endpoint2, data={"hey":"naaa"},json={"pratyush":"hello world to me"})
print(get_response.json())