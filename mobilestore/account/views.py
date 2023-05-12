from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView,View
from .forms import RegForm,LogForm
from .models import Custuser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class Home(TemplateView):
    template_name="home.html"
    
class Reg(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=Custuser
    success_url=reverse_lazy("h")
    
class home(TemplateView):
    template_name="home.html"
    
    
class Log(FormView):
    template_name="login.html"
    form_class=LogForm
    
    def post(self,request,*args,**kwargs):
            f=LogForm(data=request.POST)
            if f.is_valid():
                p=f.cleaned_data.get("password")
                u=f.cleaned_data.get("username")
                user=authenticate(request,username=u,password=p)
                if user:
                    if user.usertype == 'customer':
                        login(request,user)
                        return redirect('chm')
                        # messages.success(request,"Login Sucessfull")
                    elif user.usertype == 'store':
                        login(request,user)
                        return redirect('sh')

                else:
                    # messages.error(request,"Login Failed")
                    return redirect("login")
                
            
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect("/")

