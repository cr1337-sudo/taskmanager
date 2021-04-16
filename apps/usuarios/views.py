from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import FormularioLogin, FormularioUsuario


# Create your views here.
class CustomLogin(LoginView):
    form_class = FormularioLogin
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class CustomRegister(FormView):
    template_name = "register.html"
    form_class = FormularioUsuario
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegister, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        # Con este if hace el request para saber si el usuario está logeado o no
        if self.request.user.is_authenticated:
            return redirect("home")
        return super(CustomRegister, self).get(request, *args, **kwargs)
