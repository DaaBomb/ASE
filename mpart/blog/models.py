from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

