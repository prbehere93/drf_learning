from cgitb import lookup
from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer
from . import serializers

class ProductAPIView(generics.RetrieveAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    