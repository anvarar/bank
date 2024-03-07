from django import forms
from .models import customer,Deposit
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount', 'description']
        
        