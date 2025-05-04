from django.contrib import admin
from .models import Employee, Role, Department

# user=ansh pass 123
# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)