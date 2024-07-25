from ..models.users import User
from ..serializers.userSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class Signup:
    def put(self, request):
        if User.user_exists:
            return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)
        content = User.register()
        serializer = UserSerializer(content, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)