from django.shortcuts import render, redirect
from .models import Grade
from professor_portal.models import Announcement
from professor_portal.models import Evals
from .models import Course
from .forms import CourseSelectionForm
from django.contrib import messages
from django.contrib import messages


def home(request):
    student = request.user.student
    courses = student.course.all()
    course_details = []
    for course in courses:
        announcements = Announcement.objects.filter(course=course)
        try:
            grade = Grade.objects.filter(student=student,course=course)
        except Grade.DoesNotExist:
            grade = None
        course_details.append({'registered_courses': course,
                'announcements_made':announcements,
                 'assigned_grades':grade})
    context = {'course_details': course_details}
    return render(request, 'student_portal/home.html', context)


def course_selection_view(request):
    user = request.user
    if request.method == 'POST':
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            selected_courses = form.cleaned_data.get('courses')
            for course in selected_courses:
                if course in user.student.course.all():
                    messages.error(request, f'You are already registered in {course}.')
                    return redirect('course-selection')
            for course in selected_courses:
                    user.student.course.add(course)
    
    form = CourseSelectionForm()
    context = {'form': form}
    return render(request, 'student_portal/course_selection.html', context)
