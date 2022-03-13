from rest_framework import viewsets

from .models import Products
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    Essentially gives us a default list of HTTP methods to modify the model

    Default methods - 
    GET - ListView and DetailView
    POST - CreateView
    PUT - Update
    PATCH - Partial Update
    DELETE - Destroy
    
    """
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    