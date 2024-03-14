from django.urls import path
from book.views import store_book,show_book,edit_book
urlpatterns=[
   
   path('',store_book,name='store_book'),  
   path('show_book/',show_book,name='show_book'),
   path('edit_book/<int:id>/', edit_book, name='edit_book'),
 ]