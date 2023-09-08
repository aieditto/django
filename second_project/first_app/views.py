from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse('from contact')
def about(request):
    return HttpResponse('from about')