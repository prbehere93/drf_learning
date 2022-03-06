import requests


my_endpoint="http://localhost:8000/api/products/3" #the last / is important in the URL, otherwise the query does not get passed by the client to the django view

get_response=requests.get(my_endpoint)
print(get_response.json())
print(get_response.status_code)