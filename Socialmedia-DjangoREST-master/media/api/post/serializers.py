from rest_framework import serializers

from .models import Post, Tag, TagMap , UserLikedTags, UserDisLikedTags

class PostSerializer(serializers.HyperlinkedModelSerializer):
    
    image = serializers.ImageField(max_length=None, default=list, allow_empty_file=False, required=False)   
    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'image1', 'image2','tags', 'likes', 'dislikes', 'created_at')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name')
class TagMapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagMap
        fields = ('post')
class UserLikedTagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLikedTags
        fields = ('tag')
class UserDisLikedTagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLikedTags
        fields = ('tag')