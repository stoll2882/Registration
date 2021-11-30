from django.db import models
from django.core import validators
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    idnumber = models.PositiveBigIntegerField()
    email = models.EmailField(blank=True)
    datecreated = models.DateTimeField(blank=True, auto_now_add=True)
    datemodified = models.DateTimeField(blank=True, auto_now=True)
    
    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        abstract = True

    def __str__(self):
        return f'PersonID: {self.id}:, Name:{self.full_name}, Student ID: {self.idnumber}, Email: {self.email}, Date Created: {self.datecreated}, Date Modified: {self.datemodified} '


# Create your models here.
class Student(Person):
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    MAJORS = [
        ('CS', 'Computer Science'),
        ('ENG', 'Engineering'),
        ('BUS', 'Business'),
        ('SC', 'Science'),
        ('LAW', 'Law'),
        ('NUR', 'Nursing'),
        ('UND', 'Undecided'),
    ]

    schoolyear = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL)
    major = models.CharField(max_length=3, choices=MAJORS)
    gpa = models.FloatField(max_length=4, blank=True)

    def __str__(self):
        return f'StudentID: {self.id}: {super(Student, self).__str__()} - Year in School: {self.schoolyear}, Major: {self.major}, GPA: {self.gpa} '

    
