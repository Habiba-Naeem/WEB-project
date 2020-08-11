from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="user_index"), 
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("register", views.register, name="register"),
]