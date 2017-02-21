__author__ = 'praveen'

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Item
from .models import Comment
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.translation import ugettext as _
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

import json

class MyRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)

    class Meta:
        model= User
        fields= ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



    def __init__(self, *args, **kwargs):
        # make the request object available to the form object
        self.request = kwargs.pop('request', None)
        super(MyRegistrationForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(MyRegistrationForm, self).clean()
        # test the google recaptcha
        url = "https://www.google.com/recaptcha/api/siteverify"
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': self.request.POST.get(u'g-recaptcha-response', None),
            'remoteip': self.request.META.get("REMOTE_ADDR", None),
            }
        data = urlencode(values).encode('utf-8')
        req = Request(url, data)
        response = urlopen(req)
        result = json.loads(response.read().decode('utf-8'))

        #  result["success"] will be True on a success
        if not result["success"]:
            raise forms.ValidationError(_(u'Only humans are allowed to submit this form.'))
        return self.cleaned_data



    def save(self, commit=True):
        user= super(MyRegistrationForm, self).save(commit= False)
        user.email= self.cleaned_data['email']
        user.first_name= self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        user.is_staff= True

        if commit:
            user.save()

        return user

class ItemForm(forms.ModelForm):

    class Meta:
        model= Item
        fields= ('title', 'description', 'pub_date')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')


class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name' , 'email' ,]