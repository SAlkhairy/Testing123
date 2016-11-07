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
    about = models.TextField()
    following = models.ManyToManyField('self',
                                       symmetrical=False,
                                       related_name='followed_by')

    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User)
    #post = models.ManyToManyField()
    #for posting replies
    text = models.TextField()
    image = models.ImageField(blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

#This should have been one with the post =P
#delete it?
class Comment(models.Model):
    user = models.ForeignKey(User)
    # shouldn't it be for a specific post as well?
    post = models.ForeignKey(Post)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text