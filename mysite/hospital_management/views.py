from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.


def index(request):
    return HttpResponse("Hello to Hospital management")


def register(request):
    return HttpResponse("Welcome to new user registration")