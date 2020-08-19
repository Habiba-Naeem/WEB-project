from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from seller.models import *
# Create your views here.

def index(request): 
    if request.user.is_authenticated:
        context ={
            "name":request.user.first_name
        }
        return render(request, 'user/index.html', context)
    return render(request, 'user/index.html')
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email).user_type
            print(user)
            if user == 1:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('user_index'))
                else:
                    messages.warning(request, "Please provide correct email and password.")
                    return JsonResponse({"success": False})
        except User.DoesNotExist:
            return JsonResponse({"Register your self as a seller first":True})
    else:
        return render(request, 'user/login.html')

def logout_user(request):
    logout(request)
    return JsonResponse({"logout": True})

def register(request):


    if request.method == 'POST':

        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                if User.objects.get(email=email):
                    messages.error(request, "Username or email already exists.")
                    return JsonResponse({"Username or email already exists": True})
            except User.DoesNotExist:
                user = User.objects.create_user(user_type=1, first_name=first_name, last_name=last_name, email=email, password=password)
                messages.success(request, "Account created")

                user_log = authenticate(request, email=email, password=password)
                login(request, user_log)

                return HttpResponseRedirect(reverse('login_user'))
        else:
            messages.error(request, "Passwords do not match")
            return  JsonResponse({"Passwords do not match": True})
    else:
        return render(request, 'user/signup.html')

def browseRestaurants(request):
    context = {
        "restaurants": Restaurant.objects.all()
    }
    return render(request,'user/browseRestaurants.html', context)

def restaurant(request, nameof):
    print(nameof)
    restaurant = Restaurant.objects.get(name=nameof)
    dishes = Dish.objects.filter(restaurant=restaurant)
    context = {
        "restaurant": restaurant,
        "dishes": dishes
    }
    return render(request, 'user/menu.html', context)