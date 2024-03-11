from django.db import models

# Create your models here.
class Bookstoremodel(models.Model):
    CATEGORY={
        ('Thriller' ,'Thriller'),
        ('Commics' , 'Commics'),
        ('Romantic' , 'Romantic'),
        ('Educational' ,'Educational'),
        ('Sci-fi' ,'Sci-fi')
    }
    id = models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    category=models.CharField(max_length=30, choices=CATEGORY)
    first_pub=models.DateTimeField() 
    last_pub=models.DateTimeField() 