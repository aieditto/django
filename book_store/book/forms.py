from django import forms
from book.models import Bookstoremodel
class BookStoreForm(forms.ModelForm):
    class Meta:
        model=Bookstoremodel
        fields= [
            'id',
            'book_name', 'author', 'category'
        ]