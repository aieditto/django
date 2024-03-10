from django.shortcuts import render
from second_app.forms import StudentForm
# Create your views here.
def home(request):
    student=StudentForm()
    return render(request,'practice.html',{'student_form':student})