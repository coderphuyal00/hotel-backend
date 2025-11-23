from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    full_name=models.CharField(max_length=50,null=False,blank=False,default='')
    email=models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=False, null=False,default='')
    username=None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.email