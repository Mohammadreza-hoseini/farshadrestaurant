# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.forms.widgets import PasswordInput, TextInput
# from django.core.exceptions import ValidationError
#
# class UserLoginForm(forms.Form):
# 	username = forms.CharField(max_length=200)
# 	password = forms.CharField(widget=forms.PasswordInput)
#
#
#
#
# class UserRegistrationForm(UserCreationForm):
# 	# full_name = forms.CharField(widget=forms.TextInput)
# 	# username = forms.CharField(max_length=200)
# 	# password = forms.CharField(widget=forms.PasswordInput)
# 	# mobile = forms.IntegerField()
# 	# address = forms.CharField(max_length=400)
# 	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	address = forms.CharField(max_length=400)
# 	phoneNumber = forms.CharField(max_length=11)
# 	phone = forms.CharField()
# 	# email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
# 	class Meta:
# 		model = User
# 		# fields = ('username', 'first_name', 'last_name', 'address','phoneNumber','phone', 'password1', 'password2',)
# 		fields = '__all__'