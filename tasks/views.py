from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import *

# Create your views here.


class CustomLogin(LoginView):
    template_name = "tasks/login.html"
    fields = "__all__"
    # Si un usuario logeado quiere ingresar a esta página se lo va a llevar a otra
    redirect_authenticated_user = True

    # Realizará la siguiente accion (return) cuando el formulario es validado exitosamente, que es llevar al usuario a la página home
    def get_success_url(self):
        return reverse_lazy("home")


class RegisterPage(FormView):
    template_name = "tasks/register.html"
    # Hereda form_class de UserCreationForm, el formulario por defecto para crear registros en django
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    # Aca se indican las acciones que se realizarán si el formulario es válido
    def form_valid(self, form):
        # Se instacia el usuario que se registró y se guarda en user
        user = form.save()
        if user is not None:
            # Si pasa el if, se hace login con los datos ingresados en el registro
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


# Se edita el método get, si se accede a la url estando logeado, se madnará a la pagina home por default

    def get(self, request, *args, **kwargs):
        # Con este if hace el request para saber si el usuario está logeado o no
        if self.request.user.is_authenticated:
            return redirect("home")


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"
    # Restringe lo que un usuario puede ver, con esto solo ve las tareas que el publica
    # get_context_data permite manejar el contexot que es enviado al tempalte y como se muestra

    def get_context_data(self, **kwargs):
        # El contexto hereda de la clase padre
        # Esto va siemper uqe se quiera cambiar el contexto
        context = super().get_context_data(**kwargs)
        # Context["tasks"] porque antes el context object fue customizado
        # Se hace un filtro y se muestran las tareas del usuario que esté logeado
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        # Siempre hacer return context al ejecutar esta funcion
        return context


class TaskCreate(CreateView):
    model = Task
    fields = ["title", "description", "complete"]
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy("home")

    # Hace que un usuario pueda publicar un post SOLO con su usuario y no con otro
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = ["title", "description", "complete"]
    template_name = "tasks/task_update.html"
    success_url = reverse_lazy("home")


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("home")


class Users(ListView):
    model = User
    template_name = "tasks/users.html"
    context_object_name = "users"


class UserTasks(ListView):
    model = User
    template_name = "tasks/user_tasks.html"
    context_object_name = "tasks"


    def get_queryset(self):  
        #self.kwargs["id"], de esa forma se pasan parametros que se obtienen por url en vistas basadas en clases
        user = User.objects.get(id = self.kwargs['id'])
        return  user.task_set.all()
