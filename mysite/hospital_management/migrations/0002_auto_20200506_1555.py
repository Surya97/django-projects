# Generated by Django 3.0.2 on 2020-05-06 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
    ]
