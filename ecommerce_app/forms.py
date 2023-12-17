from django import forms
from django.contrib.auth.models import User
from .models import Cart

class MyForm(forms.ModelForm):
    myfield = forms.MultipleChoiceField(choices=User, widget=forms.SelectMultiple)
    class Meta:
        model = Cart
        fields = "__all__"