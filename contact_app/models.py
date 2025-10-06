from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ("admin", 'Admin'),
        ("user", 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.name} {self.role}"