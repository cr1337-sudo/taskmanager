from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="usuario:login"), name="logout"),
    path("register/", CustomRegister.as_view(), name="register")
]
