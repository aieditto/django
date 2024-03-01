from django.shortcuts import render
from . forms import ContactForm
# Create your views here.
def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def form(request):
    return render (request,'form.html')

def form_data(request):
    print(request.POST)
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        return render(request,'form_data.html',{'name':name, 'email':email})
    else:
        return render(request,'form_data.html')
    
def django_form(request):
    form = ContactForm(request.POST) #to show the value from website write here between the braces  request.POST
    if form.is_valid(): 
        print(form.cleaned_data)
    return render (request,"django_form.html",{'form':form})
    
    