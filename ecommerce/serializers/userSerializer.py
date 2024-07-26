from rest_framework import serializers
from ..models.users import UserInfo
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'name', 'email', 'password']