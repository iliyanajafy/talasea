from django.shortcuts import render
from blog.models import Blog
# Create your views here.



def home(request):
   best_blogs = Blog.objects.order_by("-created")[:6]
   return render(request,"home.html",{"best_blogs":best_blogs})
