from django.db import models

# Create your models here.
class check_date(models.Model):
    date = models.DateField()
    work_title = models.CharField(max_length = 34)
