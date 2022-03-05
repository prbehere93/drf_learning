from django.shortcuts import render
# from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from products.serializers import ProductSerializer

# Create your views here.

# def api_home(request, *args, **kwargs):
#     body=request.body
#     data={}
#     try:
#         data=json.loads(body) #data to python dict
#     except:
#         pass
#     print(data)
#     print(request.GET) #get the GET request params
#     data['headers']=dict(request.headers)
#     data['content-type']=request.content_type
#     data['params']=dict(request.GET)
#     return JsonResponse(data)

@api_view(["GET","POST"]) #this is a part of the DRF (it accepts a list of the allowed methods)
def api_home(request):
    """
    DRF view
    """
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        print(serializer.data)
    return Response(serializer.data)