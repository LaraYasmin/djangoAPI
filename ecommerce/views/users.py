from ..models.users import UserInfo
from rest_framework.response import Response
from rest_framework import status
from ..serializers.userSerializer import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class UsersInfoData(APIView):
    def get(self, request):
        users = UserInfo.list_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)