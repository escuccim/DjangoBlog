from  django import forms
from blog.models import Comment, Author
from django.contrib.auth.models import User


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
        fields = ('body','parent_id')

class UserForm(BootstrapModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = {'username', 'email', 'password'}

class UserProfileForm(BootstrapModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Author
        fields = {'first_name', 'last_name', 'image'}
