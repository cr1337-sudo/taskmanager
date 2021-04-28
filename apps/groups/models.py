from django.db import models
from django.conf import settings
import uuid


# Create your models here.

class Group(models.Model):
    PIN = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True, blank = True, related_name="admin")
    group_moderators = models.ManyToManyField(settings.AUTH_USER_MODEL, null = True, blank = True, related_name="group_moderators")
    group_members = models.ManyToManyField(settings.AUTH_USER_MODEL, null = True, blank = True, related_name="group_members")
    group_name = models.CharField(max_length=60, null = False, blank = False)
    #PIN = models.CharField(max_length = 100, default = "PIN", null = True, blank = True)

    def __str__(self):
        return self.group_name


