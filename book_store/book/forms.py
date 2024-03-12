from django import forms
from book.models import Bookstoremodel
class BookStoreForm(forms.ModelForm):
    class Meta:
        model=Bookstoremodel
        exclude= [
            'first_pub',
            'last_pub',
        ]