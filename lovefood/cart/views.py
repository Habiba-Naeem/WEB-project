from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import json
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to view cart.")
        return HttpResponseRedirect(reverse("user_index"))

    cart = Cart.objects.get(user=request.user)

    context = {
        "user": request.user,
        "cart_items": Cart_Item.objects.filter(cart=cart)
    }
    return render(request, "cart/index.html", context)

def cart_item(request, item):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("cart"))

    stuff = json.loads(item)
    print(stuff)
    
    try:
        cart = Cart.objects.get(user = request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user = request.user)

    restaurant = Restaurant.objects.get(id=int(stuff["restaurantid"]))
    dish = Dish.objects.get(id=int(stuff["dishid"]), restaurant=restaurant)
    product = Product.objects.create(dish=dish)
    cart_item = Cart_Item.objects.create(product = product, cart = cart)
         
    return JsonResponse({"success": True})
         
def cancel(request, id):
    cart_item = Cart_Item.objects.get(id = id)
    cart_item.delete()

    return JsonResponse({"success": True})

def quantity(request, id, q):
    try:
        cart = Cart.objects.get(user = request.user)
        cart_item = Cart_Item.objects.get(id = id)
        cart_item.quantity = q
        cart_item.save()
        return JsonResponse({"success":True})
    except:
        return JsonResponse({"success":False})    

def order(request):
    if request.method == "POST":

        cart = Cart.objects.get(user = request.user)
        cart_item = Cart_Item.objects.filter(cart = cart)
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")
        total = request.POST.get("total")
        print(total)

        user = User.objects.get(email="h@g.com")
        print(user)
        deliverer = Deliverer.objects.get(user=user)
        print(deliverer)

        for item in cart_item:
        
            order_items = Order_Items.objects.create(product = item.product, quantity=item.quantity, cart = item.cart)
            order = Order.objects.create(user=request.user ,order_items = order_items, address=address, phone_number=phone_number, total = total, deliverer=deliverer) 
            cart_item = Cart_Item.objects.get(id = item.id)
            cart_item.delete()

        return JsonResponse({"success": True})
    return JsonResponse({"Success":False})