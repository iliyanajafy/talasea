from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.register,name="login"),
    path("update/",views.update,name="update"),
    path("logout/",views.logout_user,name="logout"),
]