from django.db import models
from Inventory.utils import storestatus
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="profile",null=True,blank=True)

    desciption = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="media",null=True,blank=True)
    quantity = models.FloatField(max_length=250)
    rate = models.FloatField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product")


class Store(models.Model):
    image = models.ImageField(upload_to="media",null=True,blank=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.FloatField(null=True)
    rate = models.FloatField(null=True)

    @property
    def totalprice(self):
        return self.quantity*self.rate
    
class Order(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    status = models.CharField(
        _("Status"), max_length=255, choices=storestatus,null=True,blank=True
    )

