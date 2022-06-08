from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from acounts.forms import SignUpForm
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get(self, request):
        context = super().get_context_data(**kwargs)
        fm = SignUpForm()
        context['form'] = fm
        return context

    def post(self, request):
        fm = SignUpForm(request.POST)
        print(fm)
        if fm.is_valid():
            fm.save()
        else:
            print('not inserteds')
            fm = SignUpForm()
        return render(request, self.template_name, {'form': fm})


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
