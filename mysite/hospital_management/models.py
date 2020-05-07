from django.db import models
from django.core.validators import RegexValidator
import datetime
from django.contrib.auth.models import User
# Create your models here.


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_joining = models.DateField('Joining date')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name


class Doctor(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    gender_choices = (('M', 'Male'),
                      ('F', 'Female'),
                      ('O', 'Other')
                      )
    gender = models.CharField(max_length=1, choices=gender_choices)
    address = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    disease_description = models.CharField(max_length=200)

    def __str__(self):
        return self.patient_id + " " + self.name

