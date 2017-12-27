from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	last_name = forms.CharField(max_length=100, required=True, help_text='Required.')
	email = forms.EmailField(max_length=200, help_text='Required. Inform a valid and unique email address.')
	image = forms.ImageField(required=False, help_text='Optional.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'image', 'password1', 'password2', )