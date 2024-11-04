from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    due_date = models.DateTimeField("Due date")
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
