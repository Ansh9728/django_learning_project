from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    # path("", views.index,  name="index"),
    # path("login/accounts/sign_up", views.register_view, name='sign_up'),
    path("accounts/sign_up", views.register_view, name='sign_up'),
    path('logout', views.logout_view, name="logout"),
    path('login', views.login_view, name="login"),
    

]