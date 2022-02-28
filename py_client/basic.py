import requests

# endpoint="https://httpbin.org/status/200/"
# endpoint2="https://httpbin.org/anything"

my_endpoint="http://localhost:8000/api"

#data is sent as form data, the json data is json data
# get_response=requests.get(endpoint2, data={"hey":"naaa"},json={"pratyush":"hello world to me"})
# print(get_response.json())

get_response=requests.get(my_endpoint, params={"abc":123}, json={"query":"some wierd text data"})
print(get_response.json())
print(get_response.status_code)