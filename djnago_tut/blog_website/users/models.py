from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("Email Required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, password, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra)
    
    
class User(AbstractUser):
    
    # remove usernme field
    username = None
    first_name = None
    last_name=None
    
    full_name=models.CharField("first_name",max_length=150, blank=False, null=False)
    email=models.EmailField("email", max_length=254, unique=True)
    age = models.IntegerField('age', null=True, blank=True)
    address = models.CharField('address', max_length=255, null=True, blank=True)
    phone_number = models.CharField('phone_number', max_length=10, unique=True, primary_key=True)
    
    def __str__(self):
        return f"{self.email}"
    
    REQUIRED_FIELDS = ['email']  #REQUIRED_FIELDS attribute is a list of field names that are required when creating a user via the createsuperuser
    USERNAME_FIELD  = 'phone_number'    # configuration tells Django to use the username field as the primary identifier during authentication
    
    class Meta:
        db_table = 'users'
        
    # @property
    # def is_anonymous(self):
    #     return False
        
    objects = UserManager()