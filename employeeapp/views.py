from django.shortcuts import render
from django.contrib import messages
from .filters import BillFilter
# Create your views here.
from employeeapp.models import Category, Order,Product,Store
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import ProductCreationForm,OrderCreationForm, User
from django_filters.views import FilterView
from django.core.mail import EmailMessage

class ProductCreate(CreateView):
    form_class = ProductCreationForm
    template_name = "product.html"
    success_url = '/product/create/'
    

class ProductList(ListView):
    model = Product
    template_name = "productlist.html"
    success_url = '/product/list/'
    context_object_name = "product_list"
    # (muni ko gareni huncha mathi ko gareni huncha)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['patient_list'] = self.get_queryset()
    #     return context

class ProductUpdate(UpdateView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Product
    form_class = ProductCreationForm
    template_name = "product.html"
    success_url = '/product/list/'    


class ProductDelete(DeleteView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Product
    template_name = "productdelete.html"
    success_url = '/product/list/'  
    

class Dashboard(ListView):
    model = Category
    template_name = "dashboard.html"
    success_url = '/dashboard/'
    context_object_name = "category_list"


class CategroyList(ListView):
    model = Category
    template_name = "category.html"
    success_url = '/product/list/'
    context_object_name = "product_list"


class OrderCreate(CreateView):
    form_class = OrderCreationForm
    template_name = "order.html"
    success_url = '/order/create/'
    
    # def get_context_data(self, **kwargs):
    #     print(self.object)
    #     context= super().get_context_data(**kwargs)
    #     quantity = Product.objects.get(id=self.object.product.id).quantity
    #     if quantity<1:
    #         context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save() ## order object
            product_object = Product.objects.get(id=self.object.product.id)          
            if product_object.quantity<1:
                messages.error(request,"Product is not available")
                return super().form_invalid(form)
            product_object.quantity-=1
            product_object.save()
            store_object = Store.objects.get(id=self.object.store.id)
            store_object.quantity+=1
            store_object.save()
            return super().form_valid(form)
        return super().form_invalid(form)


class OrderList(ListView):
    model = Order
    template_name = "orderlist.html"
    success_url = '/order/list/'
    context_object_name = "order_list"
    # (muni ko gareni huncha mathi ko gareni huncha)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['patient_list'] = self.get_queryset()
    #     return context

class OrderUpdate(UpdateView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Order
    form_class = OrderCreationForm
    template_name = "order.html"
    success_url = '/order/list/'    


class OrderDelete(DeleteView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Order
    template_name = "orderdelete.html"
    success_url = '/order/list/'  
    

class StoreList(ListView):
    model = Store
    template_name = "store.html"
    success_url = '/store/list/'
    context_object_name = "store_list"    


class BillList(FilterView):
    model = Store
    template_name = "bill.html"
    success_url = '/bill/list/'
    context_object_name = "bill_list"        
    filterset_class = BillFilter
    # def get_queryset(self):
    #     q = self.request.GET.get("q")
    #     return super().get_queryset().filter(Q(name__icontains=q) | Q(address__icontains=q))
    
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.get_queryset())
    #     context['filter'] = self.get_queryset()
    #     print(context['filter'])
    #     return context
    
class Contact(TemplateView):
    template_name = 'contact.html'

class AboutUs(TemplateView):
    template_name = 'aboutus.html'    


def sendemail(request):
    print('hey')
    data=""
    print(type(request.user.id))
    register=User.objects.filter(id=request.user.id)
    if register:
        register=User.objects.get(id=request.user.id)
        if request.method=="POST":
            rec=request.POST['to']
            subject=request.POST['subject']
            message=request.POST['message']
            print(rec,subject,message)
            try:
                em=EmailMessage(subject,message,to=[rec])
                em.send()
                data="Email sent"
                return render(request,'sendemail.html',{"data":data})
            except:
                data="Could not sent please check internet connection/Email address"
        return render(request,'sendemail.html',{"data":data})
    else:
        return render(request,'sendemail.html',{'data':"Sorry you don't have data"})    
    return render(request,'sendemail.html')  