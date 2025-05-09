from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    must_be_done = models.DateTimeField()

# Create your models here.
