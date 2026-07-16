from django.db import models

# Create your models here.
from django.db import models
from reservations.models import Reservation
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    reservation = models.OneToOneField(Reservation,on_delete=models.CASCADE,related_name="payment")
    amount = models.IntegerField()
    status = models.CharField(max_length=10,choices=[("pending", "Pending"),("success", "Success"),("failed", "Failed"),],default="pending")
    gateway_ref = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Payment #{self.payment_id}"