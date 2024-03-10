from django.urls import path
from second_app.views import home

urlpatterns = [
    path('',home,name="homepage"),
]
