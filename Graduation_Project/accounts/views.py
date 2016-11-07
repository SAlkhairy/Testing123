from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.models import Post
from accounts.forms import CommonProfileForm, PostForm, EditCommonProfileForm



def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('timeline'))
    else:
        return HttpResponseRedirect(reverse('home'))


def home(request):
    #I need a sign-in option
    return HttpResponse('Hello -trial-')



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

    return HttpResponseRedirect()



@login_required
def add_post(request):
    try:
         post = request.user.post
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('timeline'))
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('timeline')
        else:
            print form.errors

    elif request.method == 'GET':
        form = PostForm(request.GET, instance=post)
        return render(request, 'accounts/***.html')

    return render(request, 'accounts/add_post.html', {'form': form })



@login_required
def edit_post(request, post_id):
    try:
        post = request.user.post(pk=post_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))

    if not request.user.is_superuser and\
    not request.user == post.user:
        raise PermissionDenied

    if request.method == 'POST':
        if post.user == request.user:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('timeline'))

    elif request.method == 'GET':
        form = PostForm(request.GET, instance=post)

    return render(request, 'accounts/edit_post.html', {'form':form} )



@login_required
def delete_post(request):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=request.POST['id'])
        if post.user == request.user:
            post.delete()
            return HttpResponseRedirect('home')
#not linked to template!


def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    #HttpResponseRedirect(reverse('edit_post')
    return render(request, 'accounts/***.html', context)



def user_media(request):
    media = Post.objects.exclude(image="")
    context = {'media': media}
    return render(request, 'accounts/user_media.html', context)



def timeline(request): # I need to come up with new terminology.
    posts = Post.objects.filter(user__in=request.user.following.all()).order_by('submission_date')
    return HttpResponseRedirect(render(request, 'accounts/timeline.html', {'posts':posts}))



@login_required
def edit_common_profile(request):
    try:
         common_profile = request.user.common_profile
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        form = EditCommonProfileForm(request.POST, instance=common_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your changes have been saved.')
            return HttpResponseRedirect(reverse('edit_common_profile'))
    elif request.method == 'GET':
        form = EditCommonProfileForm(instance=common_profile)


    return render(request, 'accounts/edit_common_profile.html', {'form':form, 'common_profile':common_profile})



def following_list(request):
    users = request.user.common_profile.following.all().order_by('follow_date')
    return render(request, 'accounts/following_list.html', {'users':users})


def followers_list(request):
    users = request.user.common_profile.followed_by.all().order_by('follow_date')
    return render(request, 'accounts/.html', {'users':users})



def search_result():
    pass