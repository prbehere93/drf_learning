from urllib import request
from rest_framework import serializers
from rest_framework.reverse import reverse # this is different than the django reverse func
from .models import Products
from .validators import validate_title

from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer): #very similar to how you make ModelForms
    owner=UserPublicSerializer(source='user',read_only=True) #to show 
    title=serializers.CharField(validators=[validate_title,]) #giving a list of validators for checking this field
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail', #takes the url name and the lookup field as args
                                             lookup_field='pk')
    body=serializers.CharField(source='content') #basically representing the 'content' field as body
    email=serializers.EmailField(write_only=True) #can only 'write' to this field (POST req)
    class Meta:
        model=Products
        fields=[
            'owner',
            'public',
            'url',
            'edit_url',
            'title',
            'email',
            'body',
            'price',
            'sale_price',
            'my_discount'
        ]
    
    # def validate_title(self,value): #the way to validate certain fields is validate_<field_name>
    #     qs=Products.objects.filter(title__iexact=value) #checking if a title already exists(adding the i in iexact ensures that the comparison is case insensitive)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    def create(self,validated_data): #can add/modify stuff while creating a new obj
        # return Products.objects.create(**validated_data)  
        email=validated_data.pop('email') #remove email from the validated data
        obj=super().create(validated_data)
        
        return obj
    
    def update(self,instance,validated_data):
        email=validated_data.pop('email') #remove email from the validated data
        return super().update(instance,validated_data)    
    
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
        
    