from django import forms 

class ContactForm(forms.Form):
    name=forms.CharField(label="Username")
    email=forms.EmailField()