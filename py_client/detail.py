import requests
from getpass import getpass

my_endpoint="http://localhost:8000/api/products/3" #the last / is important in the URL, otherwise the query does not get passed by the client to the django view
auth_endpoint='http://localhost:8000/api/auth/'
username=input('type your username\n')
password=getpass('type your password\n')
auth_response=requests.post(auth_endpoint,json={"username":username,
                                                "password":password})
print(auth_response)
if auth_response.status_code==200:
    token=auth_response.json()['token']
    headers={
        "Authorization":f"Token {token}"
    }
    get_response=requests.get(my_endpoint,headers=headers)    
    print(get_response.json())
else:
    print("Authorization not successfull")