from django.urls import path
# from .import models
# from .import views
from first_app.views import home,delete_student

urlpatterns=[
    path('',home, name="homepage"),
    path('delete_student/<int:roll>',delete_student, name='delete_student')
]