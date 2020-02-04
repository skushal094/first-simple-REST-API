"""
models file containing models for app profile_app
"""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    """Model for which API will be created"""
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.name
