from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=64)
    email =  models.EmailField(unique=True)
    username = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.email