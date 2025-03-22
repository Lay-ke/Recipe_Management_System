from django.shortcuts import render
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserProfileSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "message": "User registered successfully", 
            "user": UserProfileSerializer(user).data
            }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        print("password", password)

        try:
            user = CustomUser.objects.get(email=email)
            print("user", user)
            if user.check_password(password):
                print("Verified")
                # Generate token
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message' : "Login successful",
                    'refresh' : str(refresh),
                    'token' : str(refresh.access_token)},
                    status=status.HTTP_200_OK)
            else:
                return Response({'error' : 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# Logout User
@api_view(['POST'])
def logout_user(request):
    try:
        request.user.auth_token.delete()
        return Response({'message' : 'Logout successful'}, status=status.HTTP_200_OK)
    except:
        return Response({'error' : 'Invalid token'})


# Get User
@api_view(['GET'])
def get_user(request):
    user = request.user
    serializer = UserProfileSerializer(data=user)
    return Response({'user' : serializer.data}, status=status.HTTP_200_OK)


# Update User
@api_view(['PUT'])
def update_user(request):
    user = request.user
    serializer = UserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Update sucessful', 'user': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

