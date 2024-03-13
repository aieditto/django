from django.db import models

class Bookstoremodel(models.Model):
    CATEGORY = [
        ('Thriller', 'Thriller'),
        ('Comics', 'Comics'),
        ('Romantic', 'Romantic'),
        ('Educational', 'Educational'),
        ('Sci-fi', 'Sci-fi')
    ]
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'ID: {self.id} , Author: {self.author} '
