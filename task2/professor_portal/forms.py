from django import forms
from student_portal.models import Course,Grade, Student
from .models import Announcement, Evals

class CourseCreationForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['name', 'department','cdc']

class CourseGradeForm(forms.ModelForm):
	class Meta:
		model = Grade
		fields = ['student', 'grade','course']

class CourseAnnouncementForm(forms.ModelForm):
	class Meta:
		model = Announcement
		fields = ['course', 'title','content','attachment']

class AddStudentForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label='Select Course')
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label='Select Student')


class CreateEvalForm(forms.ModelForm):
	class Meta:
		model = Evals
		fields = ['test', 'marks','course']