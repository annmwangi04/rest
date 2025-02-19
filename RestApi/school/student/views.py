from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer  # Ensure this is correct

class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()  # Fetch all students
        serializer = StudentSerializer(students, many=True)  # Serialize data

       
        return Response(serializer.data, status=200)  # Return JSON response
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data =request.data)
          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
           return Response(serializer.errors, status=400)