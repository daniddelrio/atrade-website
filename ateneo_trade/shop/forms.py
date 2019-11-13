from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from shop.models import Profile, Item
from django import forms

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('school','major','grad_year','contact_num','fb_link')

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('price','description','category','location')