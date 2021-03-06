from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.forms import modelformset_factory

from . models import Profile, CustomQuestion

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
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
            #placeholder for each field to update only changed field. otherwise this has to go through
            #overriding save method which is tedious since user can't submit an empty/null value
            if hasattr(kwargs['instance'], field):
                if getattr(kwargs['instance'], field) == None or getattr(kwargs['instance'], field) =='':
                    self.fields[field].widget.attrs['placeholder'] = field
                else:
                    self.fields[field].widget.attrs['placeholder'] = getattr(kwargs['instance'], field)

CustomQuestionFormset = modelformset_factory(
    CustomQuestion,
    fields=('question', ),
    extra=1,
    widgets={
        'question': forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Question Here'
            }
        )
    }
)