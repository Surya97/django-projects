from django.db import models
from django.core.validators import RegexValidator
import datetime


# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=50)
    date_of_joining = models.DateTimeField('Joining date')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)