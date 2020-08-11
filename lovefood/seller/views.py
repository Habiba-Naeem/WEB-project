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
from seller.models import *
# Create your views here.

def index(request):  
    if not request.user.is_authenticated:
        return render(request, 'seller/index.html')
    
    user = User.objects.get(email=request.user.email)
    seller_name = str(user.seller.name)
    return HttpResponseRedirect(reverse("seller", args=(seller_name,)))

def login_seller(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request, email=email, password=password)
    
    if user is not None:
        login(request, user)
        user = User.objects.get(email=request.user.email)
        seller_name = str(user.seller.name)
        return HttpResponseRedirect(reverse("seller", args=(seller_name,)))

        #return HttpResponseRedirect(reverse("seller"))
        #return JsonResponse({"success": True})
    else:
        return render(request, "seller/index.html", {"message": "Invalid credentials."})

        #messages.warning(request, "Please provide correct username and password.")
        #return JsonResponse({"success": False})

def logout_seller(request):
    logout(request)
    return JsonResponse({"logout": True})

def seller(request, seller_name):
    context = {
        "seller_name" : seller_name, 
    }
    return render(request, 'seller/seller.html', context)


def register_seller(request):

    if request.method == 'POST':

        name = request.POST.get('restaurant_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        home = request.POST.get('homeornot')
        homeornot = False
        if home == 'yes':
            homeornot = True

        if password == confirm_password:
            try:
                if  User.objects.get(email=email):
                    messages.error(request, "Username or email already exists.")
                    return JsonResponse({"Username or email already exists": True})
            except User.DoesNotExist:
                user = User.objects.create_user(user_type=2, email=email, password=password)
                seller = Seller.objects.create(user=user,name=name, address=address, contact=contact,homeornot=homeornot )
                messages.success(request, "Account created")

                user_log = authenticate(request, email=email, password=password)
                login(request, user_log)
                user = User.objects.get(email=request.user.email)
                seller_name = str(user.seller.name)
                return HttpResponseRedirect(reverse("seller", args=(seller_name,)))
        else:
            messages.error(request, "Passwords do not match")
            return  JsonResponse({"Passwords do not match": True})

    if request.method == 'GET':
        return HttpResponseRedirect(reverse("seller_index"))

def getlist(request, seller_name):
    itemlist = []
    user = User.objects.get(email=request.user.email)
    seller = user.seller
    dishes = seller.cooks.all()
    count = str(dishes.count())

    '''
    for i in range(0, int(count)):
        itemlist.append(str(dishes[i].name))
    '''
    for i in range(0, int(count)):
        itemlist.append({"dish_id": int(dishes[i].id), "dish_name": str(dishes[i].name)})


    return JsonResponse({
        "itemlist": itemlist
    })


def getitem(request, seller_name, dish_id):
    user = User.objects.get(email=request.user.email)
    seller = user.seller
    dish = seller.cooks.get(pk=dish_id)
    glutten_free = "No"
    customizable = "No"
    if dish.glutten_free == True:
        glutten_free = "Yes" 
    
    if dish.customizable == True:
        customizable = "Yes" 

    item = {"name" : str(dish.name), "summary" : str(dish.summary), "nationality" : str(dish.nationality), "no_of_serving" : int(dish.no_of_serving),"picture" : str(dish.picture), "category" : str(dish.category) , "glutten_free" : glutten_free, "customizable" : customizable}
    return JsonResponse({
        "item": item
    })
'''
def item(request, seller_name, dish_id):
    return HttpResponseRedirect(reverse("redirectitem", args=(seller_name, dish_id,)))
'''
def redirectitem(request, seller_name, dish_id):
    if request.method == 'GET':    
        glutten_freeornot = "No"
        customizableornot = "No" 
        user = User.objects.get(email=request.user.email)
        seller = user.seller
        dish = seller.cooks.get(pk=dish_id)
            
        if dish.glutten_free == True:
            glutten_freeornot = "Yes"

        if dish.customizable == True:
            customizableornot = "Yes"

        context = {
            "seller_name": str(seller_name),
            "dish_id": int(dish.id),
            "name" : str(dish.name), 
            "summary" : str(dish.summary), 
            "nationality" : str(dish.nationality), 
            "no_of_serving" : int(dish.no_of_serving),
            "picture" : str(dish.picture), 
            "category" : str(dish.category) , 
            "glutten_free" : str(glutten_freeornot), 
            "customizable" : str(customizableornot)
        }
    return render(request, 'seller/item.html', context)



def additem(request, seller_name):
    user = User.objects.get(email=request.user.email)
    seller_name = str(user.seller.name)
    context = {
        "seller_name" : seller_name, 
    }
    return render(request, 'seller/additem.html', context)

def itemadded(request, seller_name):
    glutten_freeornot = False
    customizableornot = False 
    
    if request.method == 'POST':
        name = request.POST.get('dish_name')
        summary = request.POST.get('dish_summary')
        nationality = request.POST.get('dish_nationality')
        no_of_serving = request.POST.get('dish_no_of_serving')
        picture = request.POST.get('dish_picture')
        category = request.POST.get('dish_category')
        glutten_free = request.POST.get('dish_glutten_free')
        customizable = request.POST.get('dish_customizable')

        if glutten_free == True:
            glutten_freeornot = True

        if customizable == True:
            customizableornot = True
        
        user = User.objects.get(email=request.user.email)
        seller = user.seller

        Dish.objects.create(name= name, summary=summary, nationality=nationality, category=category, no_of_serving=no_of_serving, picture=picture, glutten_free=glutten_freeornot, customizable=customizableornot, seller=seller)
    context = {
        "message" : "Item added!", 
    }
    return HttpResponseRedirect(reverse("additem", args=(seller_name,)))

def deleteitem(request, seller_name, dish_id):
    user = User.objects.get(email=request.user.email)
    seller = user.seller
    dish = seller.cooks.get(pk=dish_id)
    dish.delete()

    return HttpResponseRedirect(reverse("seller", args=(seller_name,)))

def updateitem(request, seller_name, dish_id):
    user = User.objects.get(email=request.user.email)
    seller = user.seller
    dish = seller.cooks.get(pk=dish_id)

    if request.method == 'GET':    
        glutten_freeornot = "No"
        customizableornot = "No" 
        user = User.objects.get(email=request.user.email)
        seller = user.seller
        dish = seller.cooks.get(pk=dish_id)
            
        if dish.glutten_free == True:
            glutten_freeornot = "Yes"

        if dish.customizable == True:
            customizableornot = "Yes"

        context = {
            "seller_name": str(seller_name),
            "dish_id": int(dish.id),
            "name" : str(dish.name), 
            "summary" : str(dish.summary), 
            "nationality" : str(dish.nationality), 
            "no_of_serving" : int(dish.no_of_serving),
            "picture" : str(dish.picture), 
            "category" : str(dish.category) , 
            "glutten_free" : str(glutten_freeornot), 
            "customizable" : str(customizableornot)
        }
    return render(request, 'seller/updateitem.html', context)

def itemupdated(request, seller_name, dish_id):
    glutten_freeornot = False
    customizableornot = False 
    
    if request.method == 'POST':
        name = request.POST.get('dish_name')
        summary = request.POST.get('dish_summary')
        nationality = request.POST.get('dish_nationality')
        no_of_serving = request.POST.get('dish_no_of_serving')
        picture = request.POST.get('dish_picture')
        category = request.POST.get('dish_category')
        glutten_free = request.POST.get('dish_glutten_free')
        customizable = request.POST.get('dish_customizable')

        if glutten_free == "Yes":
            glutten_freeornot = True

        if customizable == "Yes":
            customizableornot = True
    
    user = User.objects.get(email=request.user.email)
    seller = user.seller
    dish = seller.cooks.get(pk=dish_id)

    dish.name = name 
    dish.summary = summary
    dish.nationality = nationality 
    dish.no_of_serving = no_of_serving
    dish.picture = picture 
    dish.category =  category 
    dish.glutten_free = glutten_freeornot
    dish.customizable = customizableornot

    dish.save()

    return HttpResponseRedirect(reverse("redirectitem", args=(seller_name, dish_id)))




  




