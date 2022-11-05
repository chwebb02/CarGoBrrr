from django import forms

# Form for inputting a username with length 64
class UsernameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)

# Form for inputting a password with length 128
class PasswordForm(forms.Form):
    password = forms.CharField(label='Password', max_length=128)

# Form for inputting a ten-digit phone number
class PhoneNumberForm(forms.Form):
    phone = forms.JSONField(label='XXXXXXXXXX')
    
# Form for inputting a location with length 100
class LocationForm(forms.Form):
    location = forms.CharField(label='Location', max_length=100)

