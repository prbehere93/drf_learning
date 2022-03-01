from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def api_home(request, *args, **kwargs):
    body=request.body
    data={}
    try:
        data=json.loads(body) #data to python dict
    except:
        pass
    print(data)
    print(request.GET) #get the GET request params
    data['headers']=dict(request.headers)
    data['content-type']=request.content_type
    data['params']=dict(request.GET)
    return JsonResponse(data)