from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import (
    Manager, Employee
)

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = "__all__"


class RegisterManagerSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = ('password', 'password2', 'email', 'first_name', 'last_name',  'dob', 'address', 'company','token')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'dob': {'required': True},
            'address': {'required': True},
            'company': {'required': True}
        }

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = Manager.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            dob=validated_data['dob'],
            address=validated_data['address'],
            company=validated_data['company']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"