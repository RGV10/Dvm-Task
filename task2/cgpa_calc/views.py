

# Create your views here.
from django.shortcuts import render

from .models import Grade
from .forms import GradeForm

def calculate_cgpa(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GradeForm()

    grades = Grade.objects.all()
    total_credit_points = sum(grade.credit_hours * grade.grade_point for grade in grades)
    total_credit_hours = sum(grade.credit_hours for grade in grades)

    if total_credit_hours == 0:
        cgpa = 0
    else:
        cgpa = total_credit_points / total_credit_hours

    context = {
        'form': form,
        'cgpa': cgpa,
    }
    return render(request, 'cgpa_calculator/calculate_cgpa.html', context)