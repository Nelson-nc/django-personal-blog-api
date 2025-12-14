from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_pic']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        profile_pic = validated_data.pop('profile_pic')
        user = User.objects.create_user(**validated_data)
        user.profile.profile_pic = profile_pic
        user.profile.save()
        return user
