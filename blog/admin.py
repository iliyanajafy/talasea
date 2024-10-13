from django.contrib import admin
from .models import Blog, Blog_author,Blog_review
# Register your models here.
admin.site.register(Blog)
admin.site.register(Blog_author)
admin.site.register(Blog_review)