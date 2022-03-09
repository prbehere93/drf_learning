from cgitb import lookup
from urllib import response
from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProductAPIView(generics.RetrieveAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self,serializer):
        """
        You can actually modify/assign/ do other stuff in this func to make changes/add more 
        things to the model before saving or send signals
        """
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        
        if content is None:
            content=title
        print(serializer)
        serializer.save(content=content)
        #send a django signal or assign a User FK to this model using request.user

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    This is a mix of CreateAPIView and ListAPIView, depending on the method (GET or POST)
    this will either list all the Products or Create new ones
    """
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self,serializer):
        """
        You can actually modify/assign/ do other stuff in this func to make changes/add more 
        things to the model before saving or send signals
        """
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        
        if content is None:
            content=title
        print(serializer)
        serializer.save(content=content)
        #send a django signal or assign a User FK to this model using request.user
    
# class ProductListAPIView(generics.ListAPIView):
#     queryset=Products.objects.all()
#     serializer_class=ProductSerializer

# @api_view(['GET','POST'])
# def product_alt_view(request,pk=None, *args, **kwargs):
#     """
#     A function based API View which is a combination of DetailAPIView and ListCreateAPIView
#     The idea here is that it will either get the 'detail' or 'list' of the model in case of a GET request
#     Or it will 'create' a model record in case of a POST request
#     """
    
#     if request.method=="GET":
#         #DetailViewAPI
#         if pk is not None:
#             obj=get_object_or_404(Products, pk=pk)
#             data=ProductSerializer(obj, many=False).data
#             return Response(data)
        
#         else:
#         #for the ListViewAPI
#             queryset=Products.objects.all()
#             data=ProductSerializer(queryset, many=True).data
#             return Response(data)
        
    
#     if request.method=="POST":
#         serializer=ProductSerializer(data=request.data)
        
#         if serializer.is_valid(raise_exception=True):
#             title=serializer.validated_data.get('title')
#             content=serializer.validated_data.get('content') or None
            
#             if content is None:
#                 content=title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({'invalid':'data not supplied in a proper format'}, status=400)
            
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
    def perform_update(self,serializer):
        """
        This method is similar to the 'perform_create' in the CreateAPIView
        """
        instance=self.get_object()
        content=serializer.validated_data.get('content')
        if not content:
            serializer.save(content=instance.title)
        else:
            serializer.save()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
    def perform_destroy(self,instance):
        #do whatever you want with the instance before destroy
        super().perform_destroy(instance)