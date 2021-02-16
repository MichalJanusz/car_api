from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass


class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)


class Rate(models.Model):
    car_id = models.ForeignKey('Car', on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
