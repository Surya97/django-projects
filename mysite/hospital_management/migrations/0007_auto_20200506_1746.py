# Generated by Django 3.0.2 on 2020-05-07 00:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management', '0006_auto_20200506_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_joining',
            field=models.DateField(verbose_name='Joining date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]