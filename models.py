from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CommonProfile(models.User):
    user = models.OneToOne()
    pet_name = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to=None, height_field=None, width_field=None)
    #I'll replace "none" with required details later
    interests = models.TextField()

class Post(models.Model):
    post_user = models.ForeignKey(CommonProfile)
    post_text = models.TextField()
    post_image = models.ImageField()
    post_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_user = models.ForeignKey(CommonProfile)
    #shouldn't it be for a specific post as well?
    comment_post = models.ForeignKey(Post)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

class Following(models.Model):
    follow_user = models.ForeignKey(CommonProfile)
    active = models.BooleanField()
    follow_date = models.DateTimeField(auto_now_add=True)
