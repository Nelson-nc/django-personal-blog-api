from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pictures", blank=True, null=True, default='profile_pictures/default_pic92.webp')

    def __str__(self):
        return self.user.username
