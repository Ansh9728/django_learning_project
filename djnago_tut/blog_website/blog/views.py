from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .permission import IsOwnerOrAdmin
from .serializers import BlogPostSerializer
from .models import BlogPost

# Create your views here.

class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    """
        this provide endpoint for read write GET and POST
    """
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    
    queryset = BlogPost.objects.all()
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff:
    #         return BlogPost.objects.all()
    #     return BlogPost.objects.filter(author=user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    
class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    " GET/PUT/PATCH/DELETE a post by ID, if you own it or are admin. "
    
    permission_classes=[IsAuthenticated, IsAdminUser]
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer