from django import forms
from .models import Course

class CourseSelection(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['name', 'department']

class CourseSelectionForm(forms.Form):
	courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())
		