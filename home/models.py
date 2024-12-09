from django.db import models
import uuid
# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    itemid = models.UUIDField(default=uuid.uuid4,primary_key=True,
                              unique=True,editable=False)
    image = models.ImageField()
    

    def __str__(self):
        return f"{self.name}"