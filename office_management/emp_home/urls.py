from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index,  name="index"),
    path("add_employee", views.add_employee, name='add_employee'),
    path("delete_emp", views.delete_emp, name='delete_emp'),
    path("delete_emp/<int:emp_id>", views.delete_emp, name='delete_emp'),
    path("update_emp", views.update_emp, name='update_emp'),
    path("update_emp/<int:emp_id>", views.update_emp, name='update_emp'),

]

