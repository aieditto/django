from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    fathers_name=models.CharField(max_length=100)
    contact_number=models.IntegerField()
    address=models.TextField()