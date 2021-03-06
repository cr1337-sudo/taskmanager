from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuarios.models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input-form'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'input-form'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

    class Meta:
        model = Usuario
        fields = ("username", "password")


class FormularioUsuario(forms.ModelForm):
    """Formulario de registro de un usuario en la base de datos
        Variables:
        -password1: Contraseña
        -password2: Contraseña validacion
    """

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'input-form',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Contraseña de Confirmación', widget=forms.PasswordInput(
        attrs={
            'class': 'input-form',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'input-form',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'input-form',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'input-form',
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'input-form',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            ),
        }
    # Validación de la contraseña,validad que ambas contraseñas ingresadas sean iguales
    # Esto antes de ser encriptadas y guardadas en la base de datos
    # Cleaned data es el date ya validado
    # Excepción: ValidationError. Cuando las claves no son iguales lanza un mensaje de error

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    # Edita el método save para que se guarde la clave luego de ser validada
    # SI commit = True se sigue con el flujo de trabajo normal preestablecido en le metodo save
    # Si commit = False guardal a instancia, la informacion que se pretende registrar
    def save(self, commit=True):
        user = super().save(commit=False)
        # Se usa set_password porque es el metodo que encripta las contraseñas, y usa pwd1 como contraseña
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user