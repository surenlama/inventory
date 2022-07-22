from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from acounts.forms import SignUpForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm
from django.views.generic import CreateView,ListView
from .forms import SignUpForm, UserAuthentiationForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = '/accounts/login/'




class Signin(View):
    template_name = 'login.html'
    form_class = UserAuthentiationForm
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        if request.method=="POST":
            fm = UserAuthentiationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
            else:

                fm = UserAuthentiationForm()
                message = "Invalid login credential"
            return render(request,self.template_name,{'form':fm,'msg':message})    
                        

# class SignUpView(TemplateView):
#     template_name = 'signup.html'

#     def get(self, request):
#         context = super().get_context_data(**kwargs)
#         fm = SignUpForm()
#         context['form'] = fm
#         return context

#     def post(self, request):
#         fm = SignUpForm(request.POST)
#         print(fm)
#         if fm.is_valid():
#             fm.save()
#         else:
#             print('not inserteds')
#             fm = SignUpForm()
#         return render(request, self.template_name, {'form': fm})


# def signup(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             # messages.success(request, "Account Created Successfully !!")
#             fm.save()
#         else:
#             fm = SignUpForm()
#             return render(request, 'signup.html', {'form': fm})
#     return HttpResponse(request, 'signup.html', {})
# def clean(self):
#     form_data = self.cleaned_data
#     if form_data['password'] != form_data['password_repeat']:
#         self._errors["password"] = ["Password do not match"] # Will raise a error message
#         del form_data['password']
#     return form_data

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')


def changepass(request):
    if request.method=="POST":
        current=request.POST['currentpass']
        change=request.POST['changepass']
        confirm=request.POST['confirmpass']
        usr=User.objects.get(id=request.user.id)
        b=usr.username
        v=usr.check_password(current)
        if v:
            if change==confirm:               
                usr.set_password(confirm)
                usr.save()
                us=User.objects.get(username=b)
                login(request,us)
                msg="Sucessfully changed password"
            else:
                msg="Password doesn't match"    
        else: 
            msg="Incorrect current password"   
        return render(request,'changepass.html',{'msg':msg})
    return render(request,'changepass.html')   