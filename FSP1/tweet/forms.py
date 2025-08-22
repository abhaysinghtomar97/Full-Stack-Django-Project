from django import forms
# from django.shortcuts import rens
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        # return render(request, 'tweet_form.html')