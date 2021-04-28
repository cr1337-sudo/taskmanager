# Generated by Django 3.1.4 on 2021-04-19 21:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_members',
            field=models.ManyToManyField(blank=True, null=True, related_name='group_members', to=settings.AUTH_USER_MODEL),
        ),
    ]