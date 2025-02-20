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
        return Response(serializer.errors, status=400)
        
    def put(self, request, *args, **kwargs):
        course = Course.objects.filter(id=kwargs['id']).first()  # Fixed: Renamed 'student' to 'course'
        if not course:
            return Response({"Error": "Course not found"}, status=404)
    
        serializer = CourseSerializer(course, data=request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)  
    
    def delete(self, request, *args, **kwargs):
        course = Course.objects.filter(id=kwargs['id']).first()

        if not course:
            return Response({"Error": "Course not found"}, status=404)

        course.delete()  
        return Response({"message": "Course deleted successfully"}, status=200)
