from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class ProductQuerySet(models.QuerySet): #custom queryset
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup= Q(title__icontains=query) | Q(content__icontains=query)
        qs=self.is_public().filter(lookup) #only searching 'public' records 
        if user:
            qs2=self.filter(user=user).filter(lookup) #will also return non-public records which belong to the user
            qs=(qs | qs2).distinct() #distinct instances of the 2 querysets
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model,using=self._db)
        
    def search(self, query, user=None):
        return self.get_queryset().search(query,user=user)
    
# Create your models here.
class Products(models.Model):
    user=models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #on deletion of user the product will not get delete
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=15, decimal_places=3, default=99.99)
    public=models.BooleanField(default=True)
    
    objects=ProductManager()
    
    @property
    def body(self): #lets just say that we want to show body instead of content in the api view, we can do it this way
        return self.content
    
    #this method is for choosing which records to show (i.e. should be indexed) using the Algolia search thing
    def is_public(self) -> bool: 
        return self.public
    
    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8)
    
    
    def discount(self):
        return (self.price-10)
    
    def __str__(self):
        return f"{self.title}"
    