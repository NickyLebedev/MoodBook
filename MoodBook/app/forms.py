"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from datetime import date

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegisterForm(UserCreationForm):
    """Registration form for new users"""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    full_name = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'First name'}))
    mail = forms.CharField(widget=forms.EmailInput({
        'class': 'form-control',
        'placeholder': 'Email'}))

    password1 = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Confirm password'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1",)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        first, second = self.cleaned_data["full_name"].split(" ")
        user.first_name = first
        user.last_name = second
        user.email = self.cleaned_data["mail"]
        user.last_login = date.today()
        if commit:
            user.save()
        return user

class EmotionsForm(ModelForm):
    pass

