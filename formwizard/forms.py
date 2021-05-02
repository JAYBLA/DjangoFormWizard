from django import forms
from .models import SignUp


class SignupForm1(forms.ModelForm):
   class Meta:
       model = SignUp
       fields = ['first_name','last_name','email',]

class SignupForm2(forms.ModelForm):
        class Meta:
            model = SignUp
            fields = ['password','password_comfirm','education_level',]