from django import forms
from apps.groups.models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("group_name", "PIN",)
    
class GroupEntryform(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("PIN", )