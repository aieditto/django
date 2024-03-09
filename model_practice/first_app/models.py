from django.db import models 

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll=models.IntegerField()
    mobile=models.IntegerField()
    subject_name=models.CharField(default="Java",max_length=20)
    
    