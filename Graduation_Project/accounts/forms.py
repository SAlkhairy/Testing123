from django.forms import ModelForm
from accounts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user','text','image','datetime']
