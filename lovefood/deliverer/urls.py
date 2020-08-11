from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="deliverer_index"), 
    path("register", views.register, name="register_deliverer"),
]