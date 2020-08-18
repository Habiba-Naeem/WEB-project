from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from user.models import User
from .models import *
# Create your views here.

def index(request, id, name): 
    if request.user.is_authenticated:
        context = {
            "name": name
        }
        return render(request, "deliverer/index.html", context)
    return HttpResponseRedirect(reverse('register_deliverer'))

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return  HttpResponseRedirect(reverse('deliverer_index', args=(request.user.id, request.user.first_name)))
        else:
            messages.warning(request, "Please provide correct email and password.")
            return JsonResponse({"success": False})
    else:
        return render(request, 'deliverer/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("register_deliverer"))


def register(request):

    if request.method == 'POST':

        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        vehicle_number = request.POST.get('vehicle_number')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                if User.objects.get(email = email):
                    messages.error(request, "Username or email already exists.")
                    return JsonResponse({"Username or email already exists": True})
            except User.DoesNotExist:
                user = User.objects.create_user(user_type = 3, email = email, first_name=first_name, last_name=last_name, password = password)
                deliverer = Deliverer.objects.create(user = user,vehicle_number = vehicle_number, phone_number = phone_number)
                messages.success(request, "Account created")

                user_log = authenticate(request, email=email, password=password)
                login(request, user_log)

                return HttpResponseRedirect(reverse('login_deliverer'))
        else:
            messages.error(request, "Passwords do not match")
            return  JsonResponse({"Passwords do not match": True})
           
    return render(request, 'deliverer/signup.html')