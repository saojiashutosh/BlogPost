from django import forms
from django.forms import ModelForm
from .models import user, blog

class UserForm(ModelForm):
    class Meta:
        model = user
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter {field.label}'  # Optional placeholder for input fields

class SigninForm(forms.Form):
    username = forms.CharField(label="Username", max_length=10)
    password = forms.CharField(label="Password", max_length=16)

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter {field.label}'  # Optional placeholder for input fields

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'content']
        labels = {
            'title': 'Blog Title',
            'content': 'Enter Blog Content'
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter {field.label}'  # Optional placeholder for input fields
