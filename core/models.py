from django.db import models
from authentication.models import User
from django.utils import timezone

# Create your models here.
class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    marks = models.CharField(max_length=20)
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class AssignmentSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    university_id = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.university_id

