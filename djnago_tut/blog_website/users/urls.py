from .views import RegisterView, UserLoginView, UserLogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view(),name='auth-register'),
    path('login/',UserLoginView.as_view(),name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', UserLogoutView.as_view(), name='logout'),
]