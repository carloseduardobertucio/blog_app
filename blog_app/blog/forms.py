from .models import Comment, Post
from django import forms
from tinymce.widgets import TinyMCE
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content')

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'content')

