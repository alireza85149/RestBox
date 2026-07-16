from django.db import models
from Villas.models import Villa
# Create your models here.
class Availability(models.Model):
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='availabilities' )
    date = models.DateField()
    status = models.CharField(max_length = 1, choices=[('A', 'available'), ('R', 'reserved'), ('N', 'not added by host')], default='A')
    jalali_date = models.CharField(max_length=10, blank=True)
    class Meta:
        unique_together = ('villa', 'date')
    def __str__(self):
        return f"{self.villa.title} - {self.jalali_date} - {self.status}"
    def save(self, *args, **kwargs):
        if self.date and not self.jalali_date:
            import jdatetime
            jdate = jdatetime.date.fromgregorian(date=self.date)
            self.jalali_date = jdate.strftime('%Y/%m/%d')
        super().save(*args, **kwargs)