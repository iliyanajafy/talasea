from django.shortcuts import render, redirect
from . import views
from .models import Blog,Blog_rating
import markdown # type: ignore
from .forms import Review
import json
from django.db.models import Avg
from django.core.paginator import Paginator

# Query to get the blog with the highest average rating

# Create your views here.

def blogs(request):
    big_blog = Blog.objects.get(title ="ارزش طلا در کشورهای مختلف جهان چگونه است؟")
    big_side = Blog.objects.filter(subject = "آموزش خرید و فروش طلا")[:3]
    popular_blog = Blog.objects.order_by("-view_count")[:5]
    latest = Blog.objects.order_by("-created")[:12]
    best_rated = Blog.objects.annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating').first()
    best_rateds = Blog.objects.annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[1:9]
    return render(request,"blogs.html",{"bigone":big_blog,"big_side":big_side,"popular_blog":popular_blog,"latest" : latest,"best_rated":best_rated,"best_rateds":best_rateds})

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
    related_blogs = Blog.objects.filter(subject=blog.subject).exclude(title=blog.title)[:4]
    subject_url = f"{blog.subject}"
    return render(request,"blog.html",{"context":blog,"reviews" : reviews,"form": form,"many":howmany,"rating": rating_av,"rating2":rating_av2,"count_rating":ratings_count,"related": related_blogs,"sub":subject_url})


def trade_gold(request):
    latest = Blog.objects.filter(subject="آموزش خرید و فروش طلا").order_by("-created")
    best_rated = Blog.objects.filter(subject="آموزش خرید و فروش طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating').first()
    best_rateds = Blog.objects.filter(subject="آموزش خرید و فروش طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[1:9]
    p = Paginator(latest,11)
    page = request.GET.get("page")
    items = p.get_page(page)

    

    return render(request,"sell.html",{"latest" : items,"best_rated":best_rated,"best_rateds":best_rateds})



def profit(request):
    latest = Blog.objects.filter(subject="سرمایه گذاری با طلا").order_by("-created")
    best_rated = Blog.objects.filter(subject="سرمایه گذاری با طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating').first()
    best_rateds = Blog.objects.filter(subject="سرمایه گذاری با طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[1:9]
    p = Paginator(latest, 11)
    page = request.GET.get("page")
    items = p.get_page(page)

    return render(request, "profit.html", {"latest": items, "best_rated": best_rated, "best_rateds": best_rateds})

def bzar(request):
    latest = Blog.objects.filter(subject="بورس و بازار جهانی").order_by("-created")
    best_rated = Blog.objects.filter(subject="بورس و بازار جهانی").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating').first()
    best_rateds = Blog.objects.filter(subject="بورس و بازار جهانی").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[1:9]
    p = Paginator(latest, 11)
    page = request.GET.get("page")
    items = p.get_page(page)

    return render(request, "bzar.html", {"latest": items, "best_rated": best_rated, "best_rateds": best_rateds})


def know(request):
    latest = Blog.objects.filter(subject="دانستنی طلا").order_by("-created")
    best_rated = Blog.objects.filter(subject="دانستنی طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating').first()
    best_rateds = Blog.objects.filter(subject="دانستنی طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[1:9]
    p = Paginator(latest, 11)
    page = request.GET.get("page")
    items = p.get_page(page)

    return render(request, "know.html", {"latest": items, "best_rated": best_rated, "best_rateds": best_rateds})


def coin(request):
    latest = Blog.objects.filter(subject="سکه طلا").order_by("-created")
    best_rated = Blog.objects.filter(subject="سکه طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating').first()
    best_rateds = Blog.objects.filter(subject="سکه طلا").annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[1:9]
    p = Paginator(latest, 11)
    page = request.GET.get("page")
    items = p.get_page(page)

    return render(request, "coin.html", {"latest": items, "best_rated": best_rated, "best_rateds": best_rateds})
