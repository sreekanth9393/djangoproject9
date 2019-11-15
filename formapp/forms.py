from django import forms
from .models import Name
class NameForm(forms.Form):
    First_name=forms.CharField(label="firstname")
    Last_name=forms.CharField(label="lastname")
