from django.shortcuts import render, redirect
from . import views
from .models import Blog
import markdown # type: ignore
from .forms import Review
# Create your views here.



def blogs(request):
    big_blog = Blog.objects.get(title ="ارزش طلا در کشورهای مختلف جهان چگونه است؟")
    return render(request,"blogs.html",{"bigone":big_blog})

def blog(request,pk):
    blog = Blog.objects.get(blogid = pk)
    blog.view_count += 1
    blog.save()
    blog.text = markdown.markdown(blog.text)
    reviews = blog.reviews.all()
    howmany = blog.reviews.count()
    form = Review()
    if request.method == 'POST':
        form = Review(request.POST)
        if form.is_valid():
            review_ = form.save(commit=False)
            review_.blog = blog
            review_.save()
    return render(request,"blog.html",{"context":blog,"reviews" : reviews,"form": form,"many":howmany})

