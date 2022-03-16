import json
from urllib import response
from getpass import getpass
import requests

endpoint="http://localhost:8000/api/products/" #for fetching the list
auth_endpoint="http://localhost:8000/api/auth/" #for generating the auth token
username=input('type your username\n')
password=getpass('type your password\n')

auth_response=requests.post(auth_endpoint,json={"username":username,
                                                "password":password})

"""
You will need to change the client after pagination has been implemented (or create a different endpoint which
will fetch all results)
"""
if auth_response.status_code==200: #if the auth is successfull
    token=auth_response.json()['token']
    headers={
        "Authorization":f"Token {token}"
    }
    get_response=requests.get(endpoint, headers=headers)
    print(get_response.json())
else:
    print("Give the correct Credentials")