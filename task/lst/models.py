from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    owner = models.ForeignKey('auth.User')
