from numpy import product
import requests

product_id=input("Please input the product_id that you want to delete")
try:
    product_id=int(product_id)
except:
    print("product id is not valid")

if product_id:
    my_endpoint=f"http://localhost:8000/api/products/{product_id}/delete/" #the last / is important in the URL, otherwise the query does not get passed by the client to the django view

get_response=requests.delete(my_endpoint)
print(get_response.status_code, get_response.status_code==204)