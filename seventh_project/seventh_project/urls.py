
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home_page'),
    path('',include("seventh_app.urls")),
]
