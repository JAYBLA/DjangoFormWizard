from django import forms
from .choices import EDUCATION_CHOICE


class SignupForm1(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

class SignupForm2(forms.Form):
    password = forms.CharField(max_length=100)
    password_comfirm = forms.CharField(max_length=100)
    education_level = forms.ChoiceField(choices=EDUCATION_CHOICE)