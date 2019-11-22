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

def feed(request):
	return render(request, 'shop/feed.html')

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

class ViewItemDetail(TemplateView):
	template_name = 'shop/item.html'
	
	def get( self, request, id ):
		item_id = id
		name = Item.objects.values('name').get(id=item_id)['name']
		price = Item.objects.values('price').get(id=item_id)['price']
		description = Item.objects.values('description').get(id=item_id)['description']
		category = Item.objects.values('category').get(id=item_id)['category']
		location = Item.objects.values('location').get(id=item_id)['location']
		seller_id = Item.objects.values('user_id').get(id=item_id)['user_id']
		seller_fn = User.objects.values('first_name').get(id=seller_id)['first_name']
		seller_ln = User.objects.values('last_name').get(id=seller_id)['last_name']
		images = Image.objects.filter(item=item_id)
		args = { 'id':item_id,'name':name, 'price':price, 'description':description, 'category':category, 'location':location, 'seller_fn':seller_fn, 'seller_ln':seller_ln, 'images':images }
		return render(request, self.template_name, args)