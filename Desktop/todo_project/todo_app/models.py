from django.db import models

# Create your models here.
class grouptable(models.Model):
    company_name=models.CharField(max_length=100,default='')
    group_name=models.CharField(max_length=100,default='')


class todolist(models.Model):
    company_name=models.CharField(max_length=100,default='')
    group_name=models.CharField(max_length=100,default='')
    username=models.CharField(max_length=100,default='')

class work_details(models.Model):
    work_title = models.CharField(max_length = 100,default = '')
    work_descript = models.TextField()
    deadline = models.DateField(null = True , blank = True)

class people_project(models.Model):
    employee = models.CharField(max_length = 100)
    group = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    work_title = models.CharField(max_length = 100)
