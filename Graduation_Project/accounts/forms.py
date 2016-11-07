from django import forms
from django.forms import ModelForm
from accounts.models import Post

from userena.forms import SignupForm

class CommonProfileForm(SignupForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ['username', 'email',
                  'password', 'human_name',
                  'pet_name', 'pet_type',
                  'profile_pic', 'about']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']


class EditCommonProfileForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'email',
                  'password', 'human_name',
                  'pet_name', 'pet_type',
                  'profile_pic', 'about']
