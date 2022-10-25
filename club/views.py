from ast import Return
from http.client import HTTPResponse
from .models import Post
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')
def vayuyana(request):
    return render(request,'vayuyana.html')
def departments(request):
    return  render(request,'departments.html')
def events(request):
    posts = Post.objects.all()
    return render(request, 'events.html', {'posts': posts})
