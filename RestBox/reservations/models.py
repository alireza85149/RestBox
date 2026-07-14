from django.db import models
from users.models import UserProfile
from Villas.models import Villa
# Create your models here.
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]
    reservation_id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='reservations')
    villa = models.ForeignKey(Villa,on_delete=models.CASCADE,related_name='reservations')
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Reservation #{self.reservation_id} - {self.guest.name} - {self.villa.Title}"