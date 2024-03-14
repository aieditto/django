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

def book_edit(request,id):
    book_model=Bookstoremodel.objects.get(pk=id)
    book_form=BookStoreForm(instance=book_model)
    if request.method=='POST':
        book=BookStoreForm(request.POST, instance=book_model)
        if book.is_valid():
            book.save()
            print(book.cleaned_data, f'data has been updated')
            return redirect('show_book')
    return render(request,'store_book.html',{'form':book_form})
    
def delete_data(request,id):
    book_model=Bookstoremodel.objects.get(pk=id).delete()
    return redirect('show_book')
    
