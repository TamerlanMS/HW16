from django import forms
from captcha.fields import CaptchaField
from .models import Post

class PostForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Post
        fields = ['title', 'content']
