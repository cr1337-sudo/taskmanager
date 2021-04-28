from django import forms
from django.db import models
from apps.groups.models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("group_name",)
    
class GroupEntryform(forms.Form):
    pin_check = forms.CharField(widget=forms.TextInput())
    