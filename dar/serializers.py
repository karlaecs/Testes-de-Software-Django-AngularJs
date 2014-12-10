from rest_framework import serializers
from dar.models import Course, Departament, Discipline, Secretariat, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'secretariat')

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('id', 'name', 'secretariats')

class DisciplineSerializer(serializers.ModelSerializer):
    disciplines = serializers.RelatedField(many=True, read_only=True)
    class Meta:
        model = Discipline
        fields = ('id', 'name', 'code', 'number_credit', 'required', 'offered', 'period_offered', 'required_credit', 'teacher', 'course', 'departament', 'disciplines', 'type')

class SecretariatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretariat
        fields = ('id', 'type', 'name', 'departament')

class StudentSerializer(serializers.ModelSerializer):
    disciplines = serializers.RelatedField(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'name', 'matriculation', 'credit_mandatory', 'credit_elective', 'matriculate', 'departament', 'disciplines', 'course', 'type')