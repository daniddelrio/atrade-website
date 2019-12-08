from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile, Item, Image
from .forms import UserForm, ProfileForm, ItemForm, ImageForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.forms import formset_factory
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

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
	return render(request, 'shop/update_profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})

@login_required
def post_item(request):
	return render(request, 'shop/post_item.html')

@login_required
def categories(request):
	return render(request, 'shop/categories.html')

def Logout(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
@transaction.atomic
def post_item(request):
	ImageFormSet = formset_factory(ImageForm, extra=5)
	
	if request.method == 'POST':
		item_form = ItemForm(request.POST)
		data = {
			'form-TOTAL_FORMS': u'1',
			'form-INITIAL_FORMS': u'0',
			'form-MAX_NUM_FORMS': u'5',
		}
		formset = ImageFormSet(request.POST, request.FILES)
		
		if item_form.is_valid() and formset.is_valid():
			item = item_form.save(commit=False)
			item.user = request.user
			item.save()
			
			for form in formset:
				if form.is_valid():
					try:
						photo = form.save(commit=False)
						photo.item = item
						photo.save()
					except:
						messages.error(request, "Database error. Please try again.")
			
			messages.success(request, 'Item uploaded successfully!')
			return HttpResponseRedirect('/')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		item_form = ItemForm(instance=request.user)
		formset = ImageFormSet()
	
	return render(request, 'shop/post_item.html', {'item_form': item_form, 'formset': formset})

class Home(ListView):
	template_name = 'shop/home.html'
	model = Item
	ordering = ['-id']

class ViewItemDetail(TemplateView):
	template_name = 'shop/item.html'

	def get( self, request, id ):
		item_id = id
		item = Item.objects.get(id=item_id)
		return render(request, self.template_name, { 'item':item })

class ViewYourItems(TemplateView):
	template_name = 'shop/profile.html'
	
	def get( self, request ):
		items = Item.objects.filter(user=request.user).order_by('-id')
		return render(request, self.template_name, { 'items':items })