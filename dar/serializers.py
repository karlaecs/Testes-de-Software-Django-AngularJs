from rest_framework import serializers
from dar.models import Course, Departament, Discipline, Secretariat, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('id', 'name')

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id', 'name', 'code', 'number_credit', 'required', 'offered', 'period_offered', 'required_credit', 'teacher')

class SecretariatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretariat
        fields = ('id', 'type', 'name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'matriculation', 'credit_mandatory', 'credit_elective')