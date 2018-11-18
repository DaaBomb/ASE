from django.db import models
import calendar
from datetime import date

# Create your models here.
class recent_activity(models.Model):

    emp_id = models.CharField(max_length =  128)
    task_done = models.CharField(max_length = 128)
    dates = models.DateField(blank = True,null = True)
    times = models.TimeField(blank = True,null = True)
