from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from .models import Register

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Returns a user instance based on the given validated token.
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            return None

        try:
            user = Register.objects.get(id=user_id)
        except Register.DoesNotExist:
            return None

        return user
    
    
class CustomHeaderJWTAuthentication(JWTAuthentication):
    """
    Read token from 'X-Api-Token' header instead of Authorization.
    """
    def get_header(self, request):
        # Look in HTTP_X_API_TOKEN instead of HTTP_AUTHORIZATION
        header = request.META.get('HTTP_X_API_TOKEN')
        if isinstance(header, str):
            return header.encode('utf-8')
        return header
    
    
