from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from ..models.users import User

class Login(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),  
        }
        return Response(content, status=status.HTTP_200_OK)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user_info = User.check_user_by_email(email)
        
        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if isinstance(user_info, str):
            return Response({"error": user_info}, status=status.HTTP_400_BAD_REQUEST)
  
        if user_info.password != password:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response("Login successful", status=status.HTTP_200_OK)