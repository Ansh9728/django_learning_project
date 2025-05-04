from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.username} and {self.email}"
    
    class Meta:
        db_table = 'users'
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True