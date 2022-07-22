from django.urls import path
from .views import Dashboard,ProductCreate,ProductList,ProductUpdate,ProductDelete,OrderCreate,OrderDelete,OrderUpdate,OrderList,StoreList,BillList,\
    AboutUs,Contact,sendemail


urlpatterns = [
    path('product/create/', ProductCreate.as_view(), name="product-create"),
    path('product/list/', ProductList.as_view(), name="product-list"),
    path('product/update/<str:pk>/', ProductUpdate.as_view(), name="product-update"),
    path('product/delete/<str:pk>/', ProductDelete.as_view(), name="product-delete"),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('order/create/', OrderCreate.as_view(), name="order-create"),
    path('order/list/', OrderList.as_view(), name="order-list"),
    path('order/update/<str:pk>/', OrderUpdate.as_view(), name="order-update"),
    path('order/delete/<str:pk>/', OrderDelete.as_view(), name="order-delete"), 
    path('store/list/', StoreList.as_view(), name="store-list"),
    path('bill/', BillList.as_view(), name="bill"),
    path('aboutus/', AboutUs.as_view(), name="aboutus"),
    path('contact/', Contact.as_view(), name="contact"),
    path('sendemail/', sendemail,name="email"),

]
