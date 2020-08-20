from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from .models import *
from seller.models import *
import json
import random
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        
            context = {
                "restaurants": Restaurant.objects.all(),
            }
            messages.warning(request, "Please login to view cart.", context)
            return render(request, "cart/index.html")

    
    try:
        cart = Cart.objects.get(user=request.user)
        try:
            orders = Order.objects.filter(user=request.user)
            context = {
                "user": request.user,
                "cart_items": Cart_Item.objects.filter(cart=cart),
                "restaurants": Restaurant.objects.all(),
                'payment_choices': payment_choice,
                "orders": orders
            }
        except Order.DoesNotExist:
            context = {
                "user": request.user,
                "cart_items": Cart_Item.objects.filter(cart=cart),
                "restaurants": Restaurant.objects.all(),
                'payment_choices': payment_choice
            }
    except Cart.DoesNotExist:
        context = {
            "user": request.user,            
            "restaurants": Restaurant.objects.all(),
            'payment_choices': payment_choice
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
    cart_item = Cart_Item.objects.create(product = product, cart = cart, total = product.dish.price)
         
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
        price = cart_item.product.dish.price
        print(price)
        cart_item.total = q * price
        cart_item.save()
        return JsonResponse({"success":True})
    except:
        return JsonResponse({"success":False})    

def order(request):
    if request.method == "POST":

        cart = Cart.objects.get(user = request.user)
        cart_item = Cart_Item.objects.filter(cart = cart)
        username =  request.POST.get("username")
        email = request.POST.get("email")
        payment = request.POST.get("payment")
        note = request.POST.get("note")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")
        total = request.POST.get("total")
        print(total)

        n =  random.randint(Deliverer.objects.all().first().pk ,  Deliverer.objects.all().last().pk)
        deliverer = Deliverer.objects.get(user__id=n)
        print(deliverer)

        for item in cart_item:
            print(item.total)
            order_items = Order_Items.objects.create(product = item.product, quantity=item.quantity,total=item.total, cart = item.cart)
            if email != request.user:
                order = Order.objects.create(user=request.user ,order_items = order_items, payment=payment, note=note ,address=address, phone_number=phone_number, total = total, deliverer=deliverer) 
                cart_item = Cart_Item.objects.get(id = item.id)
                cart_item.delete()
            else:
                messages.success(request,"Enter correct email.")
                return render(request, "cart/index.html", context)
        messages.success(request,"Order has been placed. It will be delivered soon.")
        return render(request, "cart/index.html")
    messages.warning(request, "Your cart is empty.")
    return render(request, "cart/index.html")