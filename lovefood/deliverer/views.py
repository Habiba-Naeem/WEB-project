from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.contrib.auth.models import User
from django.contrib import messages
from user.models import *
# Create your views here.

def index(request):  
    return render(request, 'deliverer/index.html')

def register(request):

    if request.method == 'POST':

        name = request.POST.get('deliverer_name')
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
                user = User.objects.create_user(user_type = 3, email = email, password = password)
                deliverer = Deliverer.objects.create(user = user,name = name, vehicle_number = vehicle_number, phone_number = phone_number)
                messages.success(request, "Account created")

                user_log = authenticate(request, email=email, password=password)
                login(request, user_log)

                return HttpResponseRedirect(reverse('login_user'))
        else:
            messages.error(request, "Passwords do not match")
            return  JsonResponse({"Passwords do not match": True})
           
    return render(request, 'deliverer/index.html')