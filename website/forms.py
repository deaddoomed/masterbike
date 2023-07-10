from django import forms
from .models import Product, Stock, Rents, ContactForm
from django.contrib.auth.forms import UserCreationForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']

class CustomUserForm(UserCreationForm):
    pass

class AddForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nombre','marca','precio','fecha']