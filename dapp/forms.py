from django import forms
from .models import Items,OrderDetail
from django.contrib.auth.models import User
from django.core import validators

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name','description','price','file']

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['customer_email','item','amount','stripe_payment_intent','has_paid']
class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(validators=[validators.validate_email])
    min_length = 2
    max_length = 30
    message_lt_min = f"Should have at least {min_length} characters."
    message_ht_max = f"Should have at most{max_length} characters."
    name_regex='\A[a-zA-Z]+\Z'
    name_message='The name accepts only letters!'
    
    username = forms.CharField(validators=[
    validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length, message_ht_max)
    ])

    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password1 = forms.CharField(label=' Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email']

    def validate_password(self):
        if self.cleaned_data['password']!= self.cleaned_data['password1']:
            raise forms.ValidationError('Password fields do not match')
        return self.cleaned_data['password1']