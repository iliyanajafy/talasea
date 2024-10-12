from django.shortcuts import render
from . import views
# Create your views here.



def blogs(request):
    return render(request,"blogs.html")

def blog(request):
    return render(request,"blog.html")