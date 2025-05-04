from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("create_person", views.create_person, name="create_person")
    path('person/', views.PersonList.as_view()),
    path('person/<int:pk_id>', views.PersonDetails.as_view())
]


