from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from dar.models import Departament, Discipline, Student, Secretariat, Course
from dar.serializers import CourseSerializer, DepartamentSerializer, DisciplineSerializer, SecretariatSerializer, StudentSerializer

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

def index(request):
    return render(request, 'dar/index.html')

class StudentList(APIView):
    parser_classes = (JSONParser,)
    serializer_class = StudentSerializer

    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = self.serializer_class(students, many=True)
        return Response(serializer.data)

