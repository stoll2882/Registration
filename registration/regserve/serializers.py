from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    model = Student
    fields = ('id', 'firstname', 'lastname', 'idnumber', 'email', 'schoolyear', 'major', 'gpa', 'datecreated', 'datemodified')
    read_only_fields = ('datecreated', 'datemodified')

    def create(self, validated_data):
        return Student(**validated_data)
        
