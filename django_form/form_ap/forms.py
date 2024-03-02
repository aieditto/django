from django import forms 

class ContactForm(forms.Form):
    name=forms.CharField(label="Username")
    email=forms.EmailField()
    age=forms.DateField()
    check =forms.BooleanField()
    FOOD= [('B','Burger'),('M','Momos'), ('Bir','Biriani')]
    food=forms.MultipleChoiceField(choices=FOOD)