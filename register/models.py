from django.db import models
from django.contrib.auth.models import User

class Custom_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    melicode = models.IntegerField(null=True,blank=True)
    year = models.IntegerField(null=True,blank=True)
    month = models.IntegerField(null=True,blank=True)
    day = models.IntegerField(null=True,blank=True)
