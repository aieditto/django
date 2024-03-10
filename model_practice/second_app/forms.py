from django import forms
from second_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        # fields=[
        #     'roll',
        #     'name',
        #     'fathers_name',
        #     'contact_number',
        #     'address'
        # ]
        fields= '__all__'