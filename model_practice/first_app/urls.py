from django.urls import path
# from .import models
from .import views

urlpatterns=[
    path('',views.home, name="homepage"),
    path('delete_student/<int:roll>',views.delete_student, name='delete_student')
]