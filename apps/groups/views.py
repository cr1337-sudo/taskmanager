from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.usuarios.models import Usuario
from apps.groups.models import Group
from tasks.models import Task
from apps.groups.forms import GroupForm, GroupEntryform
from tasks.forms import TaskForm
from django.views.generic import CreateView, ListView, View, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.db.models import Q

from django.shortcuts import get_object_or_404


from django.views.generic.base import ContextMixin
from django.utils.functional import cached_property


# Create your views here.
"""
GroupIndex:
    Hay que filtrar por usuario para saber qué tarea está realizando casa usuario
    Optimizar las "tareas de administrador" para usarlas dentro de grupos (se debe mostrar en color azul en el feed del grupo del usuario
        al que se le haya asignado una tarea por parte de un admin)
"""


class GroupIndex(View):
    model = Group
    template_name = "groups/group_index.html"
    form_class = TaskForm

    def get_queryset(self):
        tasks = Task.objects.filter(group_task=self.kwargs["pk"])
        return tasks

    def get_context_data(self, **kwargs):
        context = {}
        context["form"] = self.form_class
        context["tasks"] = self.get_queryset()
        context["group"] = self.model.objects.get(pk=self.kwargs["pk"])
        context["group_name"] = self.model.objects.get(
            group_name=context["group"])
        context["members"] = context["group"].group_members.all()
        context["user_tasks"] = context["tasks"].filter(user = self.request.user.id)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.group_task = self.model.objects.get(
                pk=self.kwargs["pk"])
            form.save()
            form.instance.user.add(self.request.user)
        return redirect("groups:group_index", pk=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class GroupTaskEdit(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_create.html"

    def get_success_url(self):
        tarea = self.model.objects.get(pk=self.kwargs["pk"])
        grupo = tarea.group_task.PIN
        return reverse_lazy("groups:group_index", kwargs={"pk": grupo})


"""
    GroupTaskDelete:
        def delete: Misma lógica para eliminar una tarea, no quedan guardadas en la DB, lo único nuevo es que al borrar la tarea 
                    se redirige al usuario hacia el grupo raiz(al fin pude)
"""


class GroupTaskDelete(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    #success_url = reverse_lazy("groups:group_list")

    def get_success_url(self):
        tarea = self.model.objects.get(pk=self.kwargs["pk"])
        grupo = tarea.group_task.PIN
        return reverse_lazy("groups:group_index", kwargs={"pk": grupo})


"""
    GoupList:

        get_queryset: Va a mostrar la lista de grupos en los que te encuentres,
        va a checkear si estás como administrador o como miembro para mostrar 
        los grupos (más adelatne agregar moderador también)

        get_context_data: Envía la lista de grupos en los que estás y el formulario
        para entrar a un nuevo grupo

        get: Renderiza template y contexto

        post: Edición del método post para ver si el código UUID enviado pertenece a algún grupo o no

"""


class GroupList(View):
    model = Group
    template_name = "groups/group_list.html"
    form_class = GroupEntryform

    def get_queryset(self):
        user = Usuario.objects.get(id=self.request.user.id)
        grupos = Group.objects.filter(
            Q(admin=user) | Q(group_members=user)
        )
        return grupos

    def get_context_data(self, **kwargs):
        context = {}
        context["groups"] = self.get_queryset
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        group = self.model.objects.get(PIN=request.POST.get("pin_check"))
        try:
            group.group_members.add(self.request.user)
        except:
            return redirect("all")
        return redirect("groups:group_list")


"""
    CreateGroup:

    post: Si el método post es llamado y el formulario es válido,
    se creará el grupo donde el admin va a ser el usuario logeado que esté creando el grupo


"""


class CreateGroup(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/create_group.html"
    succes_url = "home"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.admin = self.request.user
            form.save()
            return redirect("home")
        return super().post(request, *args, **kwargs)
