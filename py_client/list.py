import json
from urllib import response
from getpass import getpass
import requests

endpoint="http://localhost:8000/api/products/" #for fetching the list
auth_endpoint="http://localhost:8000/api/auth/" #for generating the auth token
username=input('type your username')
password=getpass('type your password')

auth_response=requests.post(auth_endpoint,json={"username":username,
                                                "password":password})


if auth_response.status_code==200: #if the auth is successfull
    token=auth_response.json()['token']
    headers={
        "Authorization":f"Token {token}"
    }
    get_response=requests.get(endpoint, headers=headers)
    print(get_response.json())