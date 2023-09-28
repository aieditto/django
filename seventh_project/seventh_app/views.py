from django.shortcuts import render

# Create your views here.
def payment(request):
    return render (request,'./seventh_apps/payment.html/')