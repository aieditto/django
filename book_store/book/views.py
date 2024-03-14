from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import Bookstoremodel
# Create your views here.
# def home(request):
#     return render(request,'store_book.html')


def store_book(request):
    # book = BookStoreForm(request.POST)
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('show_book')
    else:
        book = BookStoreForm()
    return render (request,'store_book.html', {'form':book})
    
def show_book(request):
    books = Bookstoremodel.objects.all()
    return render(request, 'show_book.html', {'books': books})

