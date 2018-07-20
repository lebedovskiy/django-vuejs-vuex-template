from posts.models import Post, Presentation, Main
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Post
        fields = ('owner', 'title', 'text', 'created_date')


class PresentationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
  
    class Meta:
        model = Presentation
        fields = ('owner', 'title', 'text', 'phone', 'e_mail', 'language', 'stack', 'skills', 'education', 'salary')


class MainSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
  
    class Meta:
        model = Main
        fields = ('owner', 'title', 'text', 'subtitle')
