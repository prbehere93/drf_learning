from asyncore import read
from rest_framework import serializers

class UserPublicSerializer(serializers.Serializer):
    """
    You can also convert this to a ModelSerializer and put a def Meta() with the model and the field names
    """
    #Note- The actual 'user' model is being used in the ProductSerializer (mentioned with the 'source' arg)
    #this is a normal serializer and not a ModelSerializer 
    id=serializers.IntegerField(read_only=True)
    username=serializers.CharField(read_only=True)
    email=serializers.EmailField(read_only=True)