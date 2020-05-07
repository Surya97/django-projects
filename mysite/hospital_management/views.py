from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import UserDetail

# Create your views here.


def index(request):
    return HttpResponse("Welcome to Hospital management")


def register(request):
    return render(request, 'register.html')


def auth(request):
    if request.method == "GET":
        return redirect('hospital_management:index')
    if request.POST['type'] == 'signup':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        joining_date = request.POST['joining-date']
        phone = request.POST['phone']
        address = request.POST['address']

        names = name.split()
        first_name = names[0]
        if len(names) == 2:
            last_name = names[1]
        else:
            last_name = ''

        user = User.objects.create(username=username, email=email, first_name=first_name,
                                   last_name=last_name)
        user.set_password(raw_password=password)
        user.save()

        user_detail = UserDetail.objects.create(user=user, date_of_joining=joining_date, phone=phone, address=address)
        user_detail.save()

        login(request, user)
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username, password=password)
        login(request, user)

    return redirect('hospital_management:home')


@login_required
def home(request):
    return render(request, 'home.html')
