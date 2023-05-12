from django import forms
from .models import Custuser
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    class Meta:
        model=Custuser
        fields=["first_name","last_name","email","phone","address","image","usertype","username","password1","password2"]
        
        
class LogForm(forms.Form):
    username=forms.CharField(max_length=500, widget=forms.TextInput(attrs={"placeholder":"enter user name","class": "form-control"}))
    password=forms.CharField(max_length=100,  widget=forms.PasswordInput(attrs={"placeholder":"Enter password","class":"form-control"}))