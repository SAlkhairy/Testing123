from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


from userena.models import UserenaBaseProfile



class CommonProfile(UserenaBaseProfile):
    user = models.OneToOneField(User)
    human_name = models.CharField(verbose_name="Human's Name", max_length=50)
    pet_name = models.CharField(verbose_name="Pet's Name",max_length=50)
    pet_type = models.CharField(verbose_name="Type of Pet",max_length=50)
    profile_pic = models.ImageField(blank=True,
                                    verbose_name="Profile Picture",
                                    upload_to=None,
                                    height_field=None,
                                    width_field=None)
    interests = models.TextField()

    def __unicode__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    image = models.ImageField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text


class Comment(models.Model):
    user = models.ForeignKey(User)
    # shouldn't it be for a specific post as well?
    post = models.ForeignKey(Post)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text


class Following(models.Model):
    user = models.ForeignKey(CommonProfile)
    # can be removed active = models.BooleanField()
    follow_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.follow_user


#below is just a trial

class RelativeUser(): #AbstractBaseUser, PermissionsMixin
relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')
class Relationship(models.Model):
from_user = models.ForeignKey(RelativeUser, related_name='from_people')
to_user = models.ForeignKey(RelativeUser, related_name='to_people')

