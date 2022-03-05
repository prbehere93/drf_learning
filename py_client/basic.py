import requests

# endpoint="https://httpbin.org/status/200/"
# endpoint2="https://httpbin.org/anything"

my_endpoint="http://localhost:8000/api/" #the last / is important in the URL, otherwise the query does not get passed by the client to the django view

#data is sent as form data, the json data is json data
# get_response=requests.get(endpoint2, data={"hey":"naaa"},json={"pratyush":"hello world to me"})
# print(get_response.json())

# get_response=requests.get(my_endpoint, params={"abc":123}, json={"query":"some wierd text data"})
get_response=requests.post(my_endpoint, params={"abc":123}, 
                           json={"ho":"hohoho","title":"some thing will be here maybe?",
                                 "price":900.9})
print(get_response.json())
print(get_response.status_code)