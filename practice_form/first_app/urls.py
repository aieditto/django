from django.urls import path
from .import views

urlpatterns=[
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name="about"),
    path('form/',views.form,name="form"),
    path('form_data/',views.form_data, name="form_data"),
]