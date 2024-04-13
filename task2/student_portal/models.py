from django.db import models
from django.contrib.auth.models import User
from login.models import CustomUser



# Create your models here.
class Department(models.Model):
	name = models.CharField(max_length=20,unique=True)

	# def __str__(self):
	# 	return self.name
 
class Course(models.Model):
	name = models.CharField(max_length=100)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	cdc = models.BooleanField()
	
	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, blank=True)
	department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True)
	course = models.ManyToManyField(Course, related_name='courses',blank=True)
 
	def __str__(self):
		return self.name

class Grade(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	grade = models.CharField(max_length=2)
	course = models.ForeignKey(Course,on_delete=models.CASCADE)

