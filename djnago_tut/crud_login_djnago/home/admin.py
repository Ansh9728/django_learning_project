from django.contrib import admin
from authenticate.models import Register
from home.models import Person

# Register your models here.
admin.site.register(Register)
admin.site.register(Person)
