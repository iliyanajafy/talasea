from django.contrib import admin
from .models import Blog, Blog_author,Blog_review,Blog_rating
# Register your models here.
admin.site.register(Blog)
admin.site.register(Blog_author)
admin.site.register(Blog_review)
admin.site.register(Blog_rating)