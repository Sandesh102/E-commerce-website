# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='homepage'),  
]