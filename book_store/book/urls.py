from django.urls import path
from book.views import store_book,show_book
urlpatterns=[
   
   path('',store_book,name='store_book'),  
   path('show_book/',show_book,name='show_book'),  

 ]