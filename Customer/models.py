from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,blank=False,null=False)
    phone_number=models.TextField(max_length=13,blank=False,null=False)
    email=models.EmailField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} customer added on{self.created_at}"