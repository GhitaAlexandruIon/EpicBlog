from django import forms
from django.db.utils import IntegrityError, ProgrammingError, OperationalError
from epicApp.models import Post, Category, Comment

try:
    choices = Category.objects.all().values_list('name', 'name')
    choice_list = []
    for item in choices:
        choice_list.append(item)
except IntegrityError as e:
    print(e)
except ProgrammingError as f:
    print(f)
except OperationalError as d:
    print(d)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'user', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
