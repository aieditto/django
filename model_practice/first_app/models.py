from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField(primary_key=True, unique=True)
    name=models.CharField(max_length=40)
    subject_name=models.CharField(max_length=50)
    college_name=models.CharField(max_length=50)
    mobile=models.IntegerField(unique=True)
    
    def __str__(self):
        return f'Roll: {self.roll}, Name: {self.name}, Mobile: {self.mobile}'