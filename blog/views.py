from django.shortcuts import render, redirect
from . import views
from .models import Blog,Blog_rating
import markdown # type: ignore
from .forms import Review
import json
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
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            rate_value = body.get('rate')
            ha = Blog_rating.objects.create(blog = blog ,rating = rate_value)
            ha.save()
        except:
            pass
    ratings = Blog_rating.objects.filter(blog=blog)
    ratings_count = ratings.count()
    if ratings_count != 0 :
        x = 0
        for i in ratings:
            x += i.rating
        rating_av = (x / ratings_count) * 20
        rating_av = f"{rating_av:.2f}" 
        rating_av2 = (x / ratings_count)
        rating_av2 = f"{rating_av2:.2f}" 
    else:
        rating_av = 0
        rating_av2 = 0
    return render(request,"blog.html",{"context":blog,"reviews" : reviews,"form": form,"many":howmany,"rating": rating_av,"rating2":rating_av2,"count_rating":ratings_count})


def trade_gold(request):
    blog = Blog.objects.filter(subject="آموزش خرید و فروش طلا")