from django.shortcuts import render
from blog.models import Blog
from . models import Shop
# Create your views here.



def home(request):
   items = Shop.objects.all()
   best_blogs = Blog.objects.order_by("-created")[:6]
   return render(request,"home.html",{"best_blogs":best_blogs,"items":items})
