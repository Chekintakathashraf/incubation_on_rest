from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=64)
    email =  models.EmailField(unique=True)
    username = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Application(models.Model):
    incubation_choices =(('Physical_Incubation','Physical_Incubation'),('Virtual_Incubation ' ,'Virtual_Incubation' ))
    status_choices =(('Registration_pending','Registration_pending'),('Registration_Under_Process ','Registration_Under_Process' ,),('Registration_rejected','Registration_rejected',))

    
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    Address = models.TextField()
    city =models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    compay_logo = models.ImageField(upload_to ='uploads/')
    team_background =  models.TextField()
    about_companyProducts  = models.TextField()
    problems = models.TextField()
    uniqueSolution = models.TextField()
    valueProposition = models.TextField()
    competativeAdvantage = models.TextField()
    revenue = models.CharField(max_length=200)
    marketsize = models.CharField(max_length=200)
    marketplan =  models.TextField()
    incubationtype = models.CharField(max_length=100, choices=incubation_choices)
    detailProposal = models.TextField()
    status =  models.CharField(max_length=100, choices=status_choices,null=True)

    def __str__(self):
        return self.company_name 