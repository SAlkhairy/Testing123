from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse

#Let's see if I know what I am doing.

from accounts.models import Post
from accounts.forms import PostForm

def home(request):
    return HttpResponseRedirect("checking it out", reverse('home'))

def add_post(request):
    form = PostForm()


def timeline(request, user_id): # I need to come up with new terminology.
    if user_id : #signed up or not...but how?
        posts = Post.objects.all()
        #needs to be "following" 's posts
        context = {'posts': posts}
        return render(request, 'base.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))


def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    #رابط تعديل؟
    return render(request, 'templates/base.html', context)

def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(instance=post)
    return


'''




def registration():
    pass

def user_page():
    pass


def search_result():
    pass

def user_settings():
    pass

def user_media():
    pass

def following():
    pass

def followers(): # I seriously need to come up with new terminology.
    pass

#add post , view post, add timeline,
'''