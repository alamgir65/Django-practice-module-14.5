from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    roll = models.AutoField(primary_key=True)
    registrant_id = models.BigIntegerField()
    Married = models.BooleanField()
    min_salary = models.SmallIntegerField()
    max_salary = models.BigIntegerField()
    About_you = models.TextField()
    
    
