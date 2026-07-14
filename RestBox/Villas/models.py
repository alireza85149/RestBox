from django.db import models
from django.contrib.auth import get_user_model
from users.models import UserProfile
# Create your models here.
User = get_user_model()

class Villa(models.Model):
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    City = models.CharField(max_length=200, verbose_name='city')
    Title = models.CharField(max_length=200, verbose_name="title")
    Address = models.TextField(verbose_name="address", unique=True)
    Capacity = models.IntegerField(verbose_name="capacity")
    Price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price_per_night")    
    def __str__(self):
        return self.Title    