from django import forms
from .models import Order
from django.contrib.auth.models import User

class OrderCreateForm(forms.ModelForm):
    address = forms.CharField( widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    first_name = forms.CharField( widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}))
    last_name = forms.CharField( widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}))
    email = forms.CharField( widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}))
    postal_code = forms.CharField( widget=forms.Textarea(attrs={'rows': 1, 'cols': 25}))
    city = forms.CharField( widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
