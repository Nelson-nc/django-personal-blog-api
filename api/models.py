from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to="posts_images", null=True, blank=True, default="posts_images/default.webp")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    votes = models.PositiveIntegerField(default=0)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Author:{self.author_id}, Post_id:{self.pk}" 

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Author:{self.author_name}, Post_id:{self.post_id.pk}, User:{self.user_id}" 