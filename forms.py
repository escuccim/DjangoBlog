from  django import forms
from blog.models import Comment, Tag, Blog
from django.contrib.auth.models import User
from django.contrib.admin import widgets

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class CommentForm(BootstrapModelForm):
    body = forms.TextInput()
    parent_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['body','parent_id']

class BlogEditForm(BootstrapModelForm):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    published_at = forms.DateTimeField(widget=forms.DateInput())
    published = forms.CheckboxInput()
    tags = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(), queryset=Tag.objects.all())

    class Meta:
        model = Blog
        fields = ['title', 'body', 'image','published', 'published_at', 'tags']
