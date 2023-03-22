from django.db import models

# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length=50)
    images = models.ImageField(max_length=None, upload_to='images/', default=list, blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True, default=0)
    dislikes = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Tag(models.Model):
	name = models.CharField(max_length=255, unique=True)
	created = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name


class TagMap(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	tag_weight = models.IntegerField(blank=True, null=True, default=1)
	created = models.DateTimeField(auto_now=True)

class UserLikedTags(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now=True)

class UserDisLikedTags(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now=True)
