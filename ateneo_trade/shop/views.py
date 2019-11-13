from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile, Item
from .forms import UserForm, ProfileForm, ItemForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

@login_required
def Home(request):
	return render(request, 'shop/home.html')

@login_required
@transaction.atomic
def update_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return HttpResponseRedirect('/')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request, 'shop/profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})

def Logout(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
@transaction.atomic
def post_item(request):
	if request.method == 'POST':
		item_form = ItemForm(request.POST)
		if item_form.is_valid():
			item = item_form.save(commit=False)
			item.user = request.user
			item.save()
			return HttpResponseRedirect('/')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		item_form = ItemForm(instance=request.user)
	return render(request, 'shop/item.html', {'item_form': item_form})