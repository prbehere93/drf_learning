from urllib import request
from rest_framework import serializers
from rest_framework.reverse import reverse # this is different than the django reverse func
from .models import Products

class ProductSerializer(serializers.ModelSerializer): #very similar to how you make ModelForms
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail', #takes the url name and the lookup field as args
                                             lookup_field='pk')
    class Meta:
        model=Products
        fields=[
            'url',
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
        
    def get_edit_url(self,obj):
        request=self.context.get('request')
        if request is None:
            return None
        return reverse("product-update", kwargs={'pk':obj.pk}, request=request)
    def get_my_discount(self,obj):
        """Essentially we can do whatever we want with the obj instance here and return what we want to the User"""
        #you have the instance of the model here, i.e. 'obj'
        #so you can actually use the obj to do stuff like grab FK's or other stuff
        if not hasattr(obj,'id'): 
            #this is basically done so that this method runs even when there is no instance of the
            #'Product' model (when there is no instance the Serializer will not work since there is no obj to get the discount from)
            return None
        if not isinstance(obj,Products):
            return None
        return obj.discount()
        
    