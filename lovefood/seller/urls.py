from django.urls import path
from . import views
from user.models import Seller
urlpatterns = [
    path("", views.index, name="seller_index"), 
    path("register", views.register_seller, name="register_seller"),
    path("login", views.login_seller, name="login_seller"),
    path("logout", views.logout_seller, name = "logout_seller"),
    path("<str:seller_name>", views.seller, name="seller"),
    path("<str:seller_name>/getlist", views.getlist, name="getlist"),
    # Displays details on the home page
    path("<str:seller_name>/get<int:dish_id>", views.getitem, name="getitem"),
    # Process and puts details on another page vis direct access
    #path("<str:seller_name>/get_dish_no_<int:dish_id>", views.item, name="item"),
    # Redriection function of the dish
    path("<str:seller_name>/<int:dish_id>", views.redirectitem, name="redirectitem"),
    # Displays a page to enter details of an item to add to the menu
    path("<str:seller_name>/additem", views.additem, name="additem"),
    # When item has been added to the menu
    path("<str:seller_name>/itemadded", views.itemadded, name="itemadded"),
    # Delete an item
    path("<str:seller_name>/<int:dish_id>/deleteitem", views.deleteitem, name="deleteitem"),
    # Open a page to update an item
    path("<str:seller_name>/<int:dish_id>/updateitem", views.updateitem, name="updateitem"),
    # Item updated
    path("<str:seller_name>/<int:dish_id>/itemupdated", views.itemupdated, name="itemupdated"),


]