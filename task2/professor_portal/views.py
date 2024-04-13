from django.shortcuts import render
from .forms import CourseCreationForm, CourseGradeForm,CourseAnnouncementForm, AddStudentForm, CreateEvalForm
from professor_portal.decorators import professor_required

@professor_required
def course_creation_view(request):
	if request.method=='POST':
		form = CourseCreationForm(request.POST)
		form.save()
	form = CourseCreationForm()
	context = {'form': form}
	return render(request, 'professor_portal/create_course.html', context)

@professor_required
def course_grade_view(request):
	if request.method=='POST':
		form = CourseGradeForm(request.POST)
		form.save()
	form = CourseGradeForm()
	context = {'form': form}
	return render(request, 'professor_portal/course_grade.html', context)

@professor_required
def course_announcement_view(request):
	if request.method=='POST':
		form = CourseAnnouncementForm(request.POST)
		form.save()
	form = CourseAnnouncementForm()
	context = {'form': form}
	return render(request, 'professor_portal/course_announcement.html', context)

@professor_required
def add_student_view(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            course = form.cleaned_data['course']
            student.course.add(course)
    else:
        form = AddStudentForm()
    return render(request, 'professor_portal/add_student.html', {'form': form})

@professor_required
def create_eval_view(request):
	if request.method=='POST':
		form = CreateEvalForm(request.POST)
		form.save()
	form = CreateEvalForm()
	context = {'form': form}
	return render(request, 'professor_portal/create_eval.html', context)

@professor_required
def home(request):
	courses = request.user.courses.all()
	context = {'registered_courses': courses}
	return render(request, 'professor_portal/home.html', context)
