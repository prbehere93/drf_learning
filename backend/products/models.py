from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    user=models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #on deletion of user the product will not get delete
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=15, decimal_places=3, default=99.99)
    
    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8)
    
    def discount(self):
        return (self.price-10)
    
    def __str__(self):
        return f"{self.title}"