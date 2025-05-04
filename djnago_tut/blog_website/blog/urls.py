from django.urls import path
from .views import BlogPostListCreateAPIView, BlogPostRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('blog/', BlogPostListCreateAPIView.as_view(), name="post-list-create"),
    path('blog/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail')
]