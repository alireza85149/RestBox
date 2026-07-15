from django.db import models
from Villas.models import Villa
# Create your models here.
class Availability(models.Model):
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='availabilities' )
    date = models.DateField()
    status = models.CharField(max_length = 1, choices=[('A', 'available'), ('R', 'reserved'), ('N', 'not added by host')], default='A')
