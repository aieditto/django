from django.urls import path
from .import views

urlpatterns = [
    path('about/',views.about, name='ab'),
    path('contact/',views.contact, name='con'),
    path('form/',views.form, name='form'),
    path('form_data/',views.form_data, name='form_d'),
    path('django_form',views.django_form,name="django_form")
]
