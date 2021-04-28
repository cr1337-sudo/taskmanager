from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from apps.groups.models import Group
from apps.groups.forms import GroupForm, GroupEntryform
from django.views.generic import CreateView, ListView, View
from django.core.exceptions import ValidationError
from django.db.models import Q


# Create your views here.
"""
GroupIndex:
    Hay que agregarle las tareas dentro del grupo.
    Hay que filtrar por usuario para saber qué tarea está realizando casa usuario
    Agregar el formulario de creación para que se creen tareas dentro del ámbito del grupo
    Optimizar las "tareas de administrador" para usarlas dentro de grupos (se debe mostrar en color azul en el feed del grupo del usuario
        al que se le haya asignado una tarea por parte de un admin)
"""
class GroupIndex(ListView):
    model = Group
    template_name = "groups/group_index.html"

    

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
