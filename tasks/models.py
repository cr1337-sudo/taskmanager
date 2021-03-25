from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    UNINITIATED = "UNINITIATED"
    IN_PROCESS = "IN PROCESS"
    READY = "READY"
    STATUS = [
        (UNINITIATED, "UNINITIATED"),
        (IN_PROCESS, "IN PROCESS"),
        (READY, "READY")
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    complete = models.CharField(max_length=100, choices = STATUS)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.title, self.date.strftime("%Y-%m-%d %H:%M:%S")) 