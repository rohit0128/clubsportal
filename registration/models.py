from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    #test = models.CharField(max_length=50 , default='')
    #dob = models.DateField(blank=True,null=True)
    #conf_status = models.BooleanField(blank=True,default=False)
    gender_choices = (
        ('M','male'),
        ('F','Female'),
        ('N','Neutral'),
    )
    gender = models.CharField(max_length=1,choices=gender_choices,default='N')
    ug_choices = (
        ('UG1','UG1'),
        ('UG2','UG2'),
        ('UG3','UG3'),
        ('UG4','UG4'),
    )
    ug = models.CharField(max_length=3,choices=ug_choices,default='UG1')

    def __str__(self):
        return self.user.username
