from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


'''
class Problems(forms.ModelForm):
	Constituency=forms.CharField(max_length=100)
	problem=forms.CharField(max_length=700)

	class Meta:
		model=Reviews
		fields=[]
'''

class UserRegistrationForm(UserCreationForm):
	FirstName=forms.CharField(max_length=100)
	LastName=forms.CharField(max_length=100)
	email=forms.EmailField()	

	class Meta:
		model=User
		fields=['FirstName','LastName','username','email','password1','password2']
