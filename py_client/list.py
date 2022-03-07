from urllib import response
import requests

endpoint="http://localhost:8000/api/products/"


data={
    "title":"testing the create.py client2",
    "price":88.88,
    "content":"something to create right here2"
}
get_response=requests.get(endpoint)
print(get_response.json())