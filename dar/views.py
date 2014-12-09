from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from dar.models import Departament, Discipline, Student, Secretariat, Course
from dar.serializers import CourseSerializer, DepartamentSerializer, DisciplineSerializer, SecretariatSerializer, StudentSerializer

from rest_framework.views import APIView
from rest_framework.decorators import api_view
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


class DisciplineList(APIView):
    parser_classes = (JSONParser,)
    serializer_class = DisciplineSerializer

    def get(self, request, format=None):
        disciplines = Discipline.objects.all()
        serializer = self.serializer_class(disciplines, many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def list_by_departament(request, departament_id):
        disciplines  = Discipline.objects.all().filter(departament=departament_id)
        serializer = DisciplineSerializer(disciplines, many=True)
        return Response(serializer.data)

class SecretariatList(APIView):
    parser_classes = (JSONParser,)
    serializer_class = SecretariatSerializer

    def get(self, request, format=None):
        secretariats = Secretariat.objects.all()
        serializer = self.serializer_class(secretariats, many=True)
        return Response(serializer.data)