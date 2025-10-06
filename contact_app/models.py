from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phonenumber = models.IntegerField(max_length=20)
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ROLE_CHOICES = [
        ("admin", 'Admin'),
        ("user", 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.firstname} {self.name} {self.role}"