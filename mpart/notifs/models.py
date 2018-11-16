from django.db import models

# Create your models here.
class Webpage(models.Model):
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name