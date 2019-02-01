from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # どのモデルを使うか
        model = Post
        # どの項目をフォームにするか
        fields = ('title', 'text')
