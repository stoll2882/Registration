from django.db import models
from django.core import validators
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    studentid = models.PositiveIntegerField(blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    schoolyear = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL)