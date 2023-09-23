from django.urls import path
from .import views

urlpatterns = [
    path('data/',views.data, name ="information"), 
    path('contact/', views.contact, name="details_contact") 
]
