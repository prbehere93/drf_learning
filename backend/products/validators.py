from rest_framework import serializers
from .models import Products

def validate_title(value): #the way to validate certain fields is validate_<field_name>
    qs=Products.objects.filter(title__iexact=value) #checking if a title already exists(adding the i in iexact ensures that the comparison is case insensitive)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name")
    return value
