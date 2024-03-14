from django.urls import path

from book.views import store_book,show_book,book_edit,delete_data

urlpatterns=[
   path('',store_book,name='store_book'),  
   path('show_book/',show_book,name='show_book'),
   path('book_edit/<int:id>',book_edit, name='book_edit'), 
   path('delete_data/<int:id>',delete_data, name='delete_data')  
]