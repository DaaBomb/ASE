from django.db import models
from django.utils import timezone

# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length=250)
    project_name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    created = models.DateField()
    due_date = models.DateField()
    time_of_submission = models.DateField(blank=True,null=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
        unique_together = ['title', 'project_name',]

class MyTodoList(models.Model):
    title = models.CharField(max_length=250)
    due_date =models.DateField()
    done = models.BooleanField(default=False)

    class Meta:
        unique_together = ['title','due_date',]

