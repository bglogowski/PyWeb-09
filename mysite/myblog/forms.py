from django import forms

from myblog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
