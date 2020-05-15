from django.urls import path
from . import views


app_name = 'hospital_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('auth/', views.auth, name="auth"),
    path('new_patient/', views.new_patient, name="new_patient"),
    path('patients/', views.patients, name="patients")
]
