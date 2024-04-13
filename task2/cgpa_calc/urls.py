from django.urls import path
from .views import calculate_cgpa

urlpatterns = [
    path('', calculate_cgpa, name='calculate_cgpa'),
]