import requests


my_endpoint="http://localhost:8000/api/products/3/update/" #the last / is important in the URL, otherwise the query does not get passed by the client to the django view

data={
    "title":"i have changed the title using a UpdateAPIView, also some code added an else block too",
    "content":"already set",
    "price":30
}
get_response=requests.put(my_endpoint,json=data)
print(get_response.json())
print(get_response.status_code)