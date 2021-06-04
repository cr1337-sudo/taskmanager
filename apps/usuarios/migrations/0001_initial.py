# Generated by Django 3.1.4 on 2021-06-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellido')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de perfil')),
                ('usuario_activo', models.BooleanField(default=True, verbose_name='Usuario activo')),
                ('usuario_administrador', models.BooleanField(default=False, verbose_name='Usuario administrador')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
