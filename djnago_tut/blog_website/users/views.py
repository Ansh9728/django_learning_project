from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.db.models import Q
from .utils import validate_email, validate_phone_number, validate_password, validate_login_credentials
# Create your views here.

class RegisterView(APIView):
    # serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        
        data = request.data
                
        validate_email(email=data.get('email'))
        validate_phone_number(phone_number=data.get('phone_number'))
        validate_password(password=data.get('password'), confirm_password=data.get('confirm_password'))
        
        serializer = RegisterSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully',
                'detail': None,
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
            
        return Response({
            "message": "Error occured during user registration",
            "detail": serializer.errors,
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)
    
  
# class UserLoginView(APIView):
#     permission_classes=[AllowAny]
    
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
        
#         if serializer.is_valid():
#             username_or_email = serializer.validated_data['username_or_email']
#             # user = User.objects.get(username=username)
            
#             # user = User.objects.filter(
#             #     Q(username=username_or_email) | Q(email=username_or_email)
#             # ).distinct().first()
            
#             user = User.objects.filter(
#                 Q(phone_number=username_or_email) | Q(email=username_or_email)
#             ).distinct().first()
            
#             print(user)
            
#             tokens = serializer.get_tokens(user)
#             return Response({
#                 'message': 'Login successful',
#                 'tokens': tokens,
#                 'user': UserSerializer(user).data
#             }, status=status.HTTP_200_OK)
            
#         return Response({
#             "message": " login Failed due to invalid credentials",
#             "detail": serializer.errors,
#             "data":None
#         }, status=status.HTTP_401_UNAUTHORIZED)



class UserLoginView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_input = serializer.validated_data['username_or_email']
        password   = serializer.validated_data['password']
        
        user = validate_login_credentials(user_input=user_input, password=password)
        
        tokens = serializer.get_tokens(user)
        return Response({
            'message': 'Login successful',
            'tokens': tokens,
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)
        
        
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        