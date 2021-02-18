from django.db import models

class TodoModel(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    archive = models.BooleanField(default=False)