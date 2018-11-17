from django.db import models

# Create your models here.
class NotificationList(models.Model):
    message = models.CharField(max_length=250)
    read = models.BooleanField(default=False)
