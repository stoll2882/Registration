from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from rest_framework import generics

# Create your views here.
def index(request):
    return HttpResponse("Hello world from Django backend!")

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer