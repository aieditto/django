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
        labels={
            'roll' : "Roll Number",
            'name' : 'User Name',
            'fathers_name':"Father's Name",
        }
        widgets={
            'roll' : forms.TextInput(attrs={'class' : 'btn-primary'}),
            'name': forms.PasswordInput()
        }
        help_texts={
            'name':'This is the username of user',
            'roll':'Confirm your roll'
        }
        error_messages={
            'name': {'required':'your name is required'}
        }