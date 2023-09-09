from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("""
                        
                        <h1>From About</h1>
                        <a href="/second_app/address/">address</a>
                        <a href="/first_app/contact/">contact</a>
                        <a href="/first_app/about/">about</a>
                        <a href="/second_app/courses/">courses</a>
                        
                        """) 
def contact(request):
    return HttpResponse("""
                        <h1>From Contact</h1>
                        <a href="/second_app/address/">address</a>
                        <a href="/first_app/contact/">contact</a>
                        <a href="/first_app/about/">about</a>
                        <a href="/second_app/courses/">courses</a>
                        """) 