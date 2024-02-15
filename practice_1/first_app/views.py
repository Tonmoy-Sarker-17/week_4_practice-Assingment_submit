from django.shortcuts import render
from . import forms
from . import models

# Create your views here.

def home(request):
    form=forms.ExampleForm()
    return render(request,'home.html',{'form':form})