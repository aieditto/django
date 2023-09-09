from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("""
                        
                        <h1>From Courses</h1>
                        <a href="/second_app/address/">address</a>
                        <a href="/first_app/contact/">contact</a>
                        <a href="/first_app/about/">about</a>
                        <a href="/second_app/courses/">courses</a>
                        """
                        ) 
def address(request):
    return HttpResponse("""
                        
                        <h1>From Address</h1>
                        <a href="/second_app/address/">address</a>
                        <a href="/first_app/contact/">contact</a>
                        <a href="/first_app/about/">about</a>
                        <a href="/second_app/courses/">courses</a>
                        """) 