from django import forms
from employeeapp.models import Product,Order
 
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image', 'description','quantity','rate','category']
        #For Label tag
        labels = {  
            'name': 'Name',
            'description': 'Description',
            'quantity': 'Quantity',
            'rate':'Rate',
            'category':'Category',
        }



#Order
class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['store', 'product','created_at']
        #For Label tag
        labels = {  
            'store': 'Store',
            'product': 'Product',
            'created_at': 'Created at',
   
        }
        