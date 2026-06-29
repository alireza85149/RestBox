from django.db import models

# Create your models here.
class UserProfile(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
