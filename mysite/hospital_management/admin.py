from django.contrib import admin
from .models import UserDetail, Doctor, Patient

# Register your models here.

admin.site.register(UserDetail)
admin.site.register(Doctor)
admin.site.register(Patient)
