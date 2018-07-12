# Create your views here.
from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('published_date')
    post = Post.objects.get(id=1)
    serializer_class = PostSerializer
