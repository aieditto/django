from django.urls import path
from .import views

urlpatterns = [
    path('payment/',views.payment),
    path('form/',views.form, name="form"),
]
