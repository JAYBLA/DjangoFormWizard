from django.db import models
from .choices import EDUCATION_CHOICE

class SignUp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password_comfirm = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100, choices=EDUCATION_CHOICE)
