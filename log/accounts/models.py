from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.{Database Table models}

class Company(models.Model): #[Table of companies ]
    company_name=models.CharField(max_length=100,default='',primary_key=True)

    def __str__(self):
        return self.company_name

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT) #or models.CASCADE
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    phone = models.IntegerField(default=0)
    company_name=models.ForeignKey(Company,default='',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

'''def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile , sender=User)'''
