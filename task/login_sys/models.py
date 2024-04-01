from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
	check_prof = models.BooleanField(default=False)
	