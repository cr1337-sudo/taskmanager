from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("user", "title", "description", "complete", "admin_task")
        labels = {
            "user": "Usuario",
            "title": "Título",
            "description": "Descripción",
            "complete": "Estado",
            "admin_task": "Tarea enviada por administrador",
        }
    widgets = {
        "user": forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        "title": forms.TextInput(
             attrs={
                    'class': 'form-control',
                    'placeholder': 'Título de la tarea'
             }
        ),
        "description": forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripción de la tarea'
            }
        ),
        "complete": forms.NullBooleanSelect(
            attrs={
                "class":"form-control",
                
            }
        ),
        "admin_task": forms.NullBooleanSelect(
            attrs={
                "class":"form-control"
            }
        )
    }


class AdminTaskForm(TaskForm):
    class Meta:
        model = Task
        fields = ("user", "title", "description", "complete", "admin_task", "user")
        labels = {
            "user": "Usuario",
            "title": "Título",
            "description": "Descripción",
            "complete": "Estado",
            "admin_task": "Tarea enviada por administrador",
        }
    widgets = {
        "user": forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        "title": forms.TextInput(
             attrs={
                    'class': 'form-control',
                    'placeholder': 'Título de la tarea'
             }
        ),
        "description": forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripción de la tarea'
            }
        ),
        "complete": forms.NullBooleanSelect(
            attrs={
                "class":"form-control",
                
            }
        ),
        "admin_task": forms.NullBooleanSelect(
            attrs={
                "class":"form-control"
            }
        )
    }
