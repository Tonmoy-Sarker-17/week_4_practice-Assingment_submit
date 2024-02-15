from django.shortcuts import render
from Albums.models import Album

# Create your views here.

def home(request):
    data = Album.objects.all()
    return render(request,'home.html',{'data':data})