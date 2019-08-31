from django.db import models

# Create your models here.
class Team(models.Model):
    tname= models.CharField(max_length=20, primary_key= True)
    team_type= models.CharField(max_length=10)
    pwd=models.charfield(max_length=20)

    class Meta:
        db_table='team'

class Information(models.Model):
    pname1=models.charfield(max_length=20)
    email1=models.EmailField(max_length=50)
    cont1=models.IntegerField(max_digits=15)
    pname2=models.charfield(max_length=20,null=True,blank=True)
    email2=models.EmailField(max_length=50,null=True,blank=True)
    cont2=models.IntegerField(max_digits=15,null=True,blank=True)
    
    class Meta:
        db_table='info'

class Answers(models.Model):
    ans1=models.
    ans2=models.
    ans3=models.