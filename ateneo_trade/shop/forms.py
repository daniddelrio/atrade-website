from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from shop.models import Profile, Item, Image
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
	def __init__(self, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs={
			'id' : 'item-name',
			'class' : 'form-control form-control-sm py-lg-3 px-lg-3',
		}
		self.fields['price'].widget.attrs={
			'id' : 'item-price',
			'class' : 'form-control form-control-sm py-lg-3 px-lg-3',
		}
		self.fields['description'].widget.attrs={
			'id' : 'item-desc',
			'class' : 'form-control form-control-sm px-lg-3',
			'rows': 5
		}
		self.fields['category'].widget.attrs={
			'id' : 'item-category',
			'class' : 'custom-select custom-select-sm px-lg-3',
		}
		self.fields['location'].widget.attrs={
			'id' : 'item-location',
			'class' : 'form-control form-control-sm py-lg-3 px-lg-3',
		}

	class Meta:
		model = Item
		fields = ('name','price','description','category','location')

class ImageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ImageForm, self).__init__(*args, **kwargs)
		self.fields['image'].widget.attrs={
			'id' : 'item-image',
			'style': 'display: none;',
			'required': False
		}
	class Meta:
		model = Image
		fields = ('image',)
		# widgets = {'image':forms.FileInput(
  #       attrs={'style':'display: none;','class':'form-control', 'required': False, } 
  #        )}