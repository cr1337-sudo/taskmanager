# Generated by Django 3.1.4 on 2021-04-19 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=60)),
                ('PIN', models.CharField(blank=True, default='PIN', max_length=100, null=True)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('group_moderators', models.ManyToManyField(blank=True, null=True, related_name='group_moderators', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]