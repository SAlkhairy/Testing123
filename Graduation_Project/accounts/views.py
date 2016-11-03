from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from accounts.models import Post
from accounts.forms import UserForm, CommonProfileForm, PostForm



def home(request):
    #home> logged in > timeline
    #home> not logged in > welcome page + sign up or sign in
    pass



def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        commonprofile_form = CommonProfileForm(data=request.POST)
        if user_form.is_valid() and commonprofile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            commonprofile = commonprofile_form.save(commit=False)
            commonprofile.user = user

            if 'profile_pic' in request.FILES:
                commonprofile.profile_pic = request.FILES['profile_pic']

            commonprofile.save()
            registered = True

        else:
            print user_form.errors, commonprofile_form.errors

    return



@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('timeline'))
        else:
            print form.errors
    else:
        form = PostForm()



@login_required
def edit_post(request):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=request.POST['id'])
        if post.user == request.user:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
        else:
            message = "You are unauthorized to edit this post."


@login_required
def delete_post(request):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=request.POST['id'])
        if post.user == request.user:
            post.delete()



def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'accounts/base.html', context)



def timeline(request, user_id): # I need to come up with new terminology.
    #planning with myself
    #home> logged in > timeline
    #home> not logged in > welcome page + sign up or sign in
    #timeline: posts of user + following , chronological order
    pass



def user_page(user_id):
    username= user_id
    return username


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
