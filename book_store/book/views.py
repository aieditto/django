from django.shortcuts import render
from book.forms import BookStoreForm
# Create your views here.
# def home(request):
#     return render(request,'store_book.html')

def store_book(request):
    book = BookStoreForm(request.POST)
    print(book)
    return render (request,'store_book.html', {'form':book})

def show_book(request):
    return render(request,'show_book.html')

def edit_book(request):
    return render(request,'edit_book.html')