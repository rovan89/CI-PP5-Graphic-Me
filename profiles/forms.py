from django.forms import ModelForm
from django import forms
from .models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile

        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
