from django import forms
from django.forms import extras
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from captcha.fields import CaptchaField
import datetime
from passwords.fields import PasswordField
from django.contrib.auth import get_user_model


MyUser = get_user_model()
YEARS = range(datetime.datetime.now().year, 
              datetime.datetime.now().year - 70, -1)


class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = PasswordField(label="Password")          
    password2 = PasswordField(label="Confirm password") 
    email = forms.EmailField(widget=forms.EmailInput)
    # first_name = forms.CharField(required=False)
    # last_name = forms.CharField(required=False)
    # phone_number = forms.CharField(required=False)
    phone_number = forms.RegexField(
        regex=r'^(\d{3}-)\d{7}$', error_message = 
        ("Phone number must be entered in the format: '067-4443322'"),
        label = "Mobile phone number", required=False, 
        help_text='Example: 067-4443322')
    birthday = forms.DateField(widget=extras.SelectDateWidget(years=YEARS), 
                               required=False)
    # avatar = forms.ImageField()
    captcha = CaptchaField()
  
    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 
                  'last_name', 'phone_number', 'birthday', 'avatar', 
                  'captcha')  

    def save(self, commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        # user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password1'])
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        # user.email = self.cleaned_data['email']
        # user.phone_number = self.cleaned_data['phone_number']
        # user.birthday = self.cleaned_data['birthday']
        # user.avatar = request.FILES['avatar']

        if commit:
            user.save()

        return user
