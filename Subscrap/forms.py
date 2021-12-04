from django import forms
from Subscrap.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

    
class SublistForm(forms.ModelForm):
	class Meta:
		model = sublist
		exclude = ['author', 'dueDate', 'startDate']
	
	


class StudentForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = students
        fields = ('email', 'username', 'password1', 'password2', )

class AccountEditForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = students
        fields = ('email', 'password1', 'password2', )


class UserEditForm(forms.ModelForm):
	class Meta:
		model = students
		fields = '__all__'
		exclude = [ 'email','password', 'is_admin', 'is_staff', 'is_active', 'is_superuser']

class SubscirptionEditForm(forms.ModelForm):
	class Meta:
		model = sublist
		fields = '__all__'
		exclude = [ 'author', 'is_notified']


class AuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = students
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class UserCheckForm(forms.ModelForm):

	class Meta:
		model = students
		fields = ('email', 'username', )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = students.objects.exclude(pk=self.instance.pk).get(email=email)
		except students.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = students.objects.exclude(pk=self.instance.pk).get(username=username)
		except students.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
