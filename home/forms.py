from django import forms
from news.models import *

class AddNews(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'image', 'slug',)