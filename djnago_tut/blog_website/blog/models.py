from django.db import models
from users.models import User
from django.conf import settings
# blog_website\blog_website\settings.py

# Create your models here.

class BlogPost(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='phone_number')
    title = models.CharField('title',max_length=200)
    content = models.TextField('content', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'blog_blogpost'
        
    def __str__(self):
        return f"Post Author is {self.author} and title {self.title}"