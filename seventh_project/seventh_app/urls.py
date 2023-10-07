from django.urls import path
from .import views

urlpatterns = [
    path('payment/',views.payment, name="payment_page"),
    path('about/',views.about, name="about_page"),
    path('form/',views.form, name="form"),
    path('djangoform/',views.Djangoform, name="djangoform"),
]
