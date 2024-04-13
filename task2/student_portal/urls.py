from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='student-home'),
    path('course-selection/', views.course_selection_view, name='course-selection'),
]
