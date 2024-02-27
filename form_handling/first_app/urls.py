from django.urls import path
from .import views

urlpatterns = [
    path('ábout/',views.about, name='ab'),
    path('contact/',views.contact, name='con'),
    path('form/',views.form, name='form'),
    path('form_data/',views.form_data, name='form_d'), 
]
