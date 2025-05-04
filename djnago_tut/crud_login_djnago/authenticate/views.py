from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import Register
from .auth import CustomJWTAuthentication

# Create your views here.

class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully',
                'detail': None,
                'data': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "Error occured during user registration",
            "detail": serializer.errors,
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            user = Register.objects.get(username=username)
            
            # Generate tokens            
            tokens = serializer.get_tokens(user=user)
            
            return Response({
                'message': 'Login successful',
                'tokens': tokens,
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            "message": " login Failed due to invalid credentials",
            "detail": serializer.errors,
            "data":None
        }, status=status.HTTP_401_UNAUTHORIZED)
        

class UserLogoutView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = Register.objects.get(id=request.user.id)
        if not user:
            return Response({
                "message": 'User not found',
                "detail": "The requested user profile could not be found.",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
            
            
        serializer = UserSerializer(user)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
            "message": "User Profile Fetched Successfully",
            "detail": None,
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    