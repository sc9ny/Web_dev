from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from . models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    botcatcher = forms.CharField(
        required=False, widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username', 'email','password1','password2']:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
