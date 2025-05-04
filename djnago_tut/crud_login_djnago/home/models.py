from django.db import models

# Create your models here.

class Person(models.Model):
    
    name = models.CharField('first_name', max_length=100)
    age = models.IntegerField('age', null=True, blank=True)
    email = models.EmailField('email', unique=True)
    address = models.CharField('address', max_length=255, null=True, blank=True)
    phone_number = models.CharField('phone_number', max_length=20, null=True, blank=True)
    date_of_birth = models.DateField('date_of_birth', null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.name} and {self.email}"
    
    class Meta:
        db_table = 'person'
        get_latest_by = ['name', 'email']

