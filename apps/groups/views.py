from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from apps.groups.models import Group
from apps.groups.forms import GroupForm, GroupEntryform
from django.views.generic import CreateView, ListView, View
from django.core.exceptions import ValidationError
from django.db.models import Q


# Create your views here.

class GroupIndex(ListView):
    model = Group
    template_name = "groups/group_index.html"

    


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
        group = self.model.objects.get(PIN=request.POST.get("PIN"))
        try:
            group.group_members.add(self.request.user)
        except:
            return redirect("all")
        return redirect("groups:group_list")


class CreateGroup(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/create_group.html"
    succes_url = "home"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        PIN = request.POST["PIN"]
        if len(PIN) < 8:
            raise ValidationError(
                "El campo PIN debe tener como mínimo 8 dígitos")
            return redirect("home")

        if form.is_valid():
            form.instance.admin = self.request.user
            form.save()
            return redirect("home")
        return super().post(request, *args, **kwargs)
