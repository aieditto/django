from django.shortcuts import render

def contact(request):
    return render (request,'./fifth_app/index.html/', {'author':'Anis', 'age':23})