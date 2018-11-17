from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

CHOICES = (
    ('CEO','CEO'),
    ('Project Manager', 'Project Manager'),
    ('Employee','Employee'),
)

# Create your models here.{Database Table models}

class Company(models.Model): #[Table of companies ]
    company_name=models.CharField(max_length=100,default='',primary_key=True)

    def __str__(self):
        return self.company_name

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT) #or models.CASCADE
    Jobtitle=models.CharField(max_length=100,default='',choices=CHOICES)
    city=models.CharField(max_length=100,default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image',blank=True)
    company_name=models.ForeignKey(Company,default='',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class teamtable(models.Model):

    company_name=models.ForeignKey(Company,default='',on_delete=models.CASCADE)
    group_name=models.CharField(max_length=100,default='')
    class Meta:
        unique_together = (('company_name', 'group_name'),)


class GroupUserTable(models.Model):
    team_details=models.ForeignKey(teamtable,default='',on_delete=models.CASCADE)
    user_name=models.ForeignKey(User,default='',on_delete=models.CASCADE)
    class Meta:
        unique_together = (('team_details', 'user_name'),)



'''def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile , sender=User)'''
