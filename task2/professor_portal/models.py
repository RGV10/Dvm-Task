from django.db import models
from django.contrib.auth.models import User
from login.models import CustomUser



from student_portal.models import Department,Course
# Create your models here.
class Prof(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE) 
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        self.user.is_prof = True
        self.user.save()
        super().save(*args, **kwargs)

        
class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    attachment = models.FileField(upload_to='announcements/', blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

class Evals(models.Model):
    test = models.FileField(upload_to='announcements/', blank=True)
    marks = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
