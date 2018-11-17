from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# Create your models here.
class ClientList(models.Model):
    name = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)
    phno = models.CharField(max_length=10,validators=[RegexValidator(regex='^.{10}$',message='length has to be 10', code='nomatch')])
    email = models.EmailField('Email', max_length=150)

    class Meta:
        unique_together = ['name','phno','email']

