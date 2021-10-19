from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime


# Create your models here.
class Assignment(models.Model):
    created_by = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=1000, default='')
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    max_credits = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'