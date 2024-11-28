# childapp/forms.py
from django import forms
from .models import Child, Video

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age', 'rights_description', 'content', 'video']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_url']

class HelpForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)