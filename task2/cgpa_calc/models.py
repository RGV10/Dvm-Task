from django.db import models

# Create your models here.
class Grade(models.Model):
    subject = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    grade_point = models.DecimalField(max_digits=3, decimal_places=2)