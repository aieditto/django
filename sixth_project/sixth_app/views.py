from django.shortcuts import render

# Create your views here.
def data(request):
    return render (request,'./sixth_app/index.html/')

def contact(request):
    return render (request,"./sixth_app/contact.html/")