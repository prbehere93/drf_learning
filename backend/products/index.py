from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Products

@register(Products)
class ProductIndex(AlgoliaIndex):
    # should_index='is_public' #refers to a method that returns a bool specifying if a record should be indexed or not
    fields=[
        'title',
        'content',
        'price',
        'user',
        'public'
    ]
    
    settings={
        'searchableAttributes':['title','content'],
        'attributesForFaceting':['user','public'],
    }