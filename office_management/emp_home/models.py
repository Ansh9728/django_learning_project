from django.db import models
from django import forms

# Create your models here.
# their may be integrity in the department and role deparment name will be same
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Role(models.Model):
    designation = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.designation


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()


    def __str__(self) -> str:
        return f"{self.first_name} {self. department}"
    

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'salary', 'phone']