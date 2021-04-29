from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile


class FixedUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    email = forms.CharField(required=True, label='', widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}),help_text=_("Remember that password should be unique, don't write 'apple' or '123'"))
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}), help_text=_("Now enter the same password as above, for verification."))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class FixedAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    class Meta:
        model = User
        fields = ('username', 'password')


class ChangeUserProfile(UserChangeForm):
    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    email = forms.CharField(required=True, label='Email', widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    first_name = forms.CharField(required=True, label='First name', widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name = forms.CharField(required=True, label='Last name', widget=forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    password = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ChangeUserPassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


# class FixedPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Enter old password'}))
#     new_password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Enter new password'}))
#     new_password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm new password'}))
#     error_messages = {'password_mismatch': _("The two password fields didn't match.")}
#     class Meta:
#         model = User
#         fields = ('old_password', 'new_password1', 'new_password2')
#
#
#     def clean_password2(self):
#         new_password1 = self.cleaned_data.get("new_password1")
#         new_password2 = self.cleaned_data.get("new_password2")
#         if new_password1 and new_password2 and new_password1 != new_password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',)


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic',]
