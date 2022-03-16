from unittest import result
from rest_framework import generics

from products.models import Products
from products.serializers import ProductSerializer

class SearchListView(generics.ListAPIView):
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