from  django import forms
from models import userModel

class signUpForm(forms.ModelForm):
    class meta:
        model= UserModel 
        fields=['email','username','name','password'] 
