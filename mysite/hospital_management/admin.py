from django.contrib import admin
from .models import UserDetail, Doctor, Patient
from django.contrib.auth import models

# Register your models here.


class UserDetailAdminView(admin.ModelAdmin):
    list_display = ('user', 'date_of_joining', 'phone')


admin.site.register(UserDetail, UserDetailAdminView)
admin.site.register(Doctor)
admin.site.register(Patient)
