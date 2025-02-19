from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer 

class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()  
        serializer = CourseSerializer(courses, many=True) 
        return Response(serializer.data, status=200)  

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data) 
        
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
