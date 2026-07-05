from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Villa(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='villas')    
    title = models.CharField(max_length=200, verbose_name="title")
    address = models.TextField(verbose_name="address")
    capacity = models.IntegerField(verbose_name="capacity")
    price_per_night = models.IntegerField(max_digits=10, verbose_name="price_per_night")
    def __str__(self):
        return self.title    