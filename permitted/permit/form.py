from django.contrib.auth.models import User
from .models import Person, Chatbox, Userinfo
from django import forms
from mongodbforms import DocumentForm

class UserReg(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLog(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class MessageForm(DocumentForm):

    class Meta:
        model = Chatbox
        fields = ['message']