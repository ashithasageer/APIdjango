from django.db.models.fields.files import ImageFileDescriptor
from rest_framework import viewsets
from .serializers import PostSerializer, TagMapSerializer, TagSerializer, UserDisLikedTagsSerializer, UserLikedTagsSerializer
from .models import Post, Tag, TagMap, UserDisLikedTags, UserLikedTags

# Create your views here.
# serialized view using viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('likes')
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagMapViewSet(viewsets.ModelViewSet):
    queryset = TagMap.objects.all()
    serializer_class = TagMapSerializer

class UserLikedTagsViewSet(viewsets.ModelViewSet):
    queryset = UserLikedTags.objects.all()
    serializer_class = UserLikedTagsSerializer
class UserDisLikedTagsViewSet(viewsets.ModelViewSet):
    queryset = UserDisLikedTags.objects.all()
    serializer_class = UserDisLikedTagsSerializer