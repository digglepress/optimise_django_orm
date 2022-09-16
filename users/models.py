from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=40)
    website = models.URLField()

    # class Meta:
    #     indexes = ['id']

    def __str__(self):
        return self.get_full_name()


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=150)
    catch_phrase = models.CharField(max_length=150)
    bs = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="address")
    street = models.CharField(max_length=55)
    suite = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    zipcode = models.CharField(max_length=55)
    geo = models.JSONField()

    def __str__(self):
        return self.street
