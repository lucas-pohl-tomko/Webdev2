from django import forms
from django.contrib.auth.models import User

from app.models import Post, Profile

from django import forms
from app.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name','description', 'document', )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'cols': 120,
                    'rows': 2
                }
            ),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about_me', 'location')
