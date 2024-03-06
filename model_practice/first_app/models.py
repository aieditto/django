from django.db import models 

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    mobile=models.IntegerField()
    subject_name=models.CharField(default="Java",max_length=20)
    
    def __str__(self):
        return  f'Student Name: {self.name}, Roll: {self.roll}' 
        
    
    