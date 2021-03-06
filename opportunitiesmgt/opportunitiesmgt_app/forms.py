from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account, Opportunitie


# Create your forms here.

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(CreateUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = '__all__'


class OpportunitieForm(ModelForm):
	class Meta:
		model = Opportunitie
		fields = '__all__'