from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='prof-home'),
    path('create-course/', views.course_creation_view, name='create-course'),
    path('course-grade/', views.course_grade_view, name='course-grade'),
    path('course-announcement/', views.course_announcement_view, name='course-announcement'),
    path('add-student/', views.add_student_view, name='add-student'),
    path('create-eval/', views.create_eval_view, name='create-eval'),
]