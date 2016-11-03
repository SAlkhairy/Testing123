from django.forms import ModelForm
from django.contrib.auth.models import User
from accounts.models import Post, CommonProfile
from django import formsclass

UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CommonProfileForm(forms.ModelForm):
    class Meta:
        model = CommonProfile
        fields = ['human_name', 'pet_name', 'pet_type', 'profile_pic', 'interests']
        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']
