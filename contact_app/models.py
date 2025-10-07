from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=20,default='DefaultName')
    email = models.EmailField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=20,  blank=True, null=True)

    ROLE_CHOICES = [
        ("user", 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.firstname} - {self.role}"
