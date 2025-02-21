from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer,UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from knox.models import AuthToken

class AuthenticationView(APIView):
     permission_classes = [AllowAny]
     def post(self, request, *args, **kwargs):
         user = authenticate(username = request.data['username'],password = request.data['password'])
         if user:
             auth_token = AuthToken.objects.create(user)[1]
             print (auth_token)
             return Response({"token": auth_token}, status =200)
         return Response({"Msg": "wrong_credentials"}, status =200) 
         
class UserregisterView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400) 
        



class StudentView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True) 
        return Response(serializer.data, status=200) 
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        student = Student.objects.filter(id=kwargs['id']).first()   # Fixed: student.object → Student.objects
        if not student:
            return Response({"Error": "Student not found"}, status=404)
    
        serializer = StudentSerializer(student, data=request.data, partial=True)  # Fixed: Serializer → serializer
        if serializer.is_valid():  # Fixed indentation
            serializer.save()  # Missing serializer.save() call
            return Response(serializer.data, status=201)  # Fixed: response → Response
        
        return Response(serializer.errors, status=400)  # Fixed: response → Response
    
    def delete(self, request, *args, **kwargs):
         student = Student.objects.filter(id=kwargs['id']).first()  # Fixed: Student.object → Student.objects

         if not student:
            return Response({"Error": "Student not found"}, status=404)

         student.delete()  # Delete the student record
         return Response({"message": "Success"}, status=200)
