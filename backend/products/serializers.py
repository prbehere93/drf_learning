from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer): #very similar to how you make ModelForms
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Products
        fields=[
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    def get_my_discount(self,obj):
        """Essentially we can do whatever we want with the obj instance here and return what we want to the User"""
        #you have the instance of the model here, i.e. 'obj'
        #so you can actually use the obj to do stuff like grab FK's or other stuff
        return obj.discount()
        