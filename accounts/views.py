from django.shortcuts import render
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status

def register_user(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)