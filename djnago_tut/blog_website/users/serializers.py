from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from django.db.models import Q


class RegisterSerializer(serializers.ModelSerializer):
    full_name=serializers.CharField(required=True, allow_blank=False)
    age=serializers.IntegerField(required=False, allow_null=True)
    address=serializers.CharField(required=False, allow_blank=True)
    # phone_number=serializers.CharField(required=False, allow_blank=True)
    phone_number=serializers.CharField(required=True, allow_blank=False)
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)
    
    class Meta:
        model  = User
        fields = [
            'full_name','email',
            'password','confirm_password',
            'age','address','phone_number'
        ]
    
    # def validate_first_name(self, value):
    #     if not value.strip():
    #         raise serializers.ValidationError("First name cannot be blank.")
    #     return value
        
    # def validate(self, attrs):
    #     # ensure password and confirm_password match
    #     if attrs.get('password') != attrs.get('confirm_password'):
    #         raise serializers.ValidationError("Passwords do not match")
        
    #     return attrs
    
    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("A user with this email already exists.")
    #     return value
    
    # def validate_phone_number(self, value):
    #     if User.objects.filter(phone_number=value).exists():
    #         raise serializers.ValidationError("The Phone Number already associated with some other user")
    #     return value
    
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        
        # Delegate creation to UserManager
        user = User.objects.create_user(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            # username=validated_data.get('username'),
            password=validated_data['password'],
            age=validated_data.get('age'),
            address=validated_data.get('address'),
            phone_number=validated_data.get('phone_number'),
        )
        return user
    
    
class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    # def validate(self, data):
    #     user_input = data.get('username_or_email')
    #     password = data.get('password')
        
    #     # user = User.objects.filter(
    #     #     Q(username=user_input) | Q(email=user_input)
    #     # ).distinct().first()
        
    #     user = User.objects.filter(
    #         Q(phone_number=user_input) | Q(email=user_input)
    #     ).distinct().first()

        
    #     if user is None:
    #         raise AuthenticationFailed("User does not exist")

    #     if not check_password(password, user.password):
    #         raise AuthenticationFailed("Incorrect password")
        
    #     return data

    
    def get_tokens(self,user):
        refresh = RefreshToken.for_user(user)
        print('re', user)
        # refresh['user_id'] = user.id  # Include the user ID in the token payload
        refresh['phone_number'] = user.phone_number
        refresh['email'] = user.email
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'phone_number']
