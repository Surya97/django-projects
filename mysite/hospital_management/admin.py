from django.contrib import admin
from .models import User, Doctor, Patient

# Register your models here.


class UserAdminView(admin.ModelAdmin):
    list_display = ('name', 'user_id')


admin.site.register(User, UserAdminView)
admin.site.register(Doctor)
admin.site.register(Patient)
