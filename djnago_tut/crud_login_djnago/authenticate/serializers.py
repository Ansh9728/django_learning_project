from rest_framework import serializers
from .models import Register
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Register
        fields = ['username', 'name', 'email', 'password', 'confirm_password']
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return Register.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        try:
            user = Register.objects.get(username=data['username'])
        except Register.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Incorrect password")
        
        return data
        
    def get_tokens(self, user):
        token = RefreshToken()
        token['user_id'] = user.id
        token['username'] = user.username
        return {
            'refresh': str(token),
            'access': str(token.access_token),
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'username', 'name', 'email', 'is_active', 'date_joined']
        read_only_fields = ['id', 'date_joined']