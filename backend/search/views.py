from unittest import result
from rest_framework import generics
from rest_framework.response import Response

from products.models import Products
from products.serializers import ProductSerializer

from .import client

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user=None
        query=request.GET.get('q')
        if request.user.is_authenticated:
            user=request.user.username
        
        public=str(request.GET.get('public'))!=0 # not sure what this does (perhaps it gives it a default value?)
        if not query:
            return Response('',status=400)
        results=client.perform_search(query,user=user,public=public) #public and user are filters
        return Response(results)
    
class OldSearchListView(generics.ListAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        qs=super().get_queryset()
        q=self.request.GET.get('q')
        results=Products.objects.none()
        if q:
            user=None
            if self.request.user.is_authenticated:
                user=self.request.user
            results=qs.search(q, user=user)
        return results