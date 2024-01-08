from django.db import models

# Create your models here.
class ProjectUser(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=30)
    DOB=models.CharField(max_length=10)
    