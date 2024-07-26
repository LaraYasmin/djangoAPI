from ..models.users import UserInfo
from ..serializers.userSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class Signup(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password or not name:
            return Response({"error": "Name, email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if UserInfo.objects.filter(email=email).exists():
            return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)
        
        user = UserInfo(name=name, email=email, password=password)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)