from urllib import response
import requests

endpoint="http://localhost:8000/api/products/create/"


data={
    "title":"testing the create.py client",
    "price":88.88,
    "content":"something to create right here"
}
get_response=requests.post(endpoint,json=data)
print(get_response.json())