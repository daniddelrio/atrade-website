from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from shop.models import Profile, Item, Image
from django import forms

class UserForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs={
			'id' : 'first-name',
			'class' : 'form-control form-control-sm',
		}
		self.fields['last_name'].widget.attrs={
			'id' : 'last-name',
			'class' : 'form-control form-control-sm',
		}
		self.fields['email'].widget.attrs={
			'id' : 'email',
			'class' : 'form-control form-control-sm',
		}

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['email_is_visible'].widget.attrs={
			'id' : 'email-switch',
			'class' : 'custom-control-input',
		}
		self.fields['school'].widget.attrs={
			'id' : 'user-school',
			'class' : 'form-control form-control-sm py-lg-3 px-lg-3',
		}
		self.fields['school_is_visible'].widget.attrs={
			'id' : 'school-switch',
			'class' : 'custom-control-input',
		}
		self.fields['major'].widget.attrs={
			'id' : 'user-major',
			'class' : 'form-control form-control-sm px-lg-3',
			'rows': 5
		}
		self.fields['grad_year'].widget.attrs={
			'id' : 'user-grad-year',
			'class' : 'form-control form-control-sm',
		}
		self.fields['gradyr_is_visible'].widget.attrs={
			'id' : 'graduation-year-switch',
			'class' : 'custom-control-input',
		}
		self.fields['contact_num'].widget.attrs={
			'id' : 'user-contact-num',
			'class' : 'form-control form-control-sm',
		}
		self.fields['fb_link'].widget.attrs={
			'id' : 'user-fb-link',
			'class' : 'form-control form-control-sm',
		}
		self.fields['display_pic'].widget.attrs={
			'id' : 'display-pic',
			'style': 'opacity: 0;'
		}

	class Meta:
		model = Profile
		fields = ('email_is_visible','school','school_is_visible','major','major_is_visible','grad_year','gradyr_is_visible','contact_num','fb_link', 'display_pic')

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
	class Meta:
		model = Image
		fields = ('image',)