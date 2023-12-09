from django import forms
from .models import Items
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name','description','price','file']

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password1 = forms.CharField(label=' Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','first_name']

    def validate_password(self):
        if self.cleaned_data['password']!= self.cleaned_data['password1']:
            raise forms.ValidationError('Password fields do not match')
        return self.cleaned_data['password1']