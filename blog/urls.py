from django.urls import path,include
from . import views
urlpatterns = [
    path("blogs/",views.blogs,name="blogs"),
    path("blog/<str:pk>/",views.blog,name="blog"),
    path('markdownx/', include('markdownx.urls')),
    path("blogs/trade",views.trade_gold,name = "آموزش خرید و فروش طلا"),
    path("blogs/invest", views.profit, name="سرمایه گذاری با طلا"),
    path("blogs/market", views.bzar, name="بورس و بازار جهانی"),
    path("blogs/coin", views.coin, name="سکه طلا"),
    path("blogs/knowledge", views.know, name="دانستنی طلا")
]

