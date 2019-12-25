from django import forms
from .models import Articles, Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'post')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
