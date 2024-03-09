from django.shortcuts import render, redirect
from .import models
# Create your views here.
def home(request):
    students=models.Student.objects.all()
    return render (request,'home.html',{'students':students})

def delete_student(request, roll):
    student_delete=models.Student.objects.get(pk= roll).delete()
    # students=models.Student.objects.all()
    print(student_delete)
    # return render (request,'home.html',{'students':students})
    return redirect('homepage')
