from django.db import models
from django.contrib.auth import get_user_model
from users.models import UserProfile
# Create your models here.
User = get_user_model()

class Villa(models.Model):
    villa_id = models.AutoField(primary_key=True)
    host_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, verbose_name='city')
    title = models.CharField(max_length=200, verbose_name="title")
    address = models.TextField(verbose_name="address", unique=True)
    capacity = models.IntegerField(verbose_name="capacity")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price_per_night")   
    amenities = models.JSONField(default=dict)  
    def __str__(self):
        return self.title  