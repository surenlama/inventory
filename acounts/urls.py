from django.contrib import admin
from django.urls import path
from acounts.views import SignUp,Signin,Logout,changepass
urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Signin.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('changepassword/', changepass,name="changepass"),
]
