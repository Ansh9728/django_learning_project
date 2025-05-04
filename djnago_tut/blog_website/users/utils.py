from rest_framework.exceptions import ValidationError
from .models import User
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password, check_password


def validate_phone_number(phone_number):    
    if User.objects.filter(phone_number=phone_number).exists():
        raise ValidationError({"phone_number": "This phone number is already registered."})
    # return phone_number


def validate_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError({"email": "This email is already registered."})
    # return email


def validate_password(password, confirm_password):
    if password.strip() != confirm_password.strip():
        raise ValidationError({"password": "password and confirm password mismatch "})
    
    
def validate_login_credentials(user_input, password):
    
    user = User.objects.filter(
            Q(phone_number=user_input) | Q(email=user_input)
        ).distinct().first()
    
    if user is None:
        raise AuthenticationFailed("User does not exist")

    if not check_password(password, user.password):
        raise AuthenticationFailed("Incorrect password")
    
    return user
    