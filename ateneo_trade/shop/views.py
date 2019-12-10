from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from django.db.models import Q
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
def profile(request):
	return render(request, 'shop/profile.html')

@login_required
def post_item(request):
	return render(request, 'shop/post_item.html')

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
	template_name = 'shop/view-profile.html'

	def get( self, request ):
		items = Item.objects.filter(user=request.user)
		return render(request, self.template_name, { 'items':items })

class Categories(TemplateView):
	template_name = 'shop/categories.html'

	def get(self, request):
		items = Item.objects.all().order_by('-id')
		category_list = []
		query = Q()
		has_query = False
		for name in range(0,12):
			category = self.request.GET.get(str(name), None)
			if( category != None ):
				if( category == 'All'):
					category_list.append(name)
					break
				query.add(Q(category=category),Q.OR)
				has_query = True
				category_list.append(name)

		if( has_query ):
			items = Item.objects.filter(query)
		else:
			items = Item.objects.all()

		sort = self.request.GET.get('order', None)
		selected_order = 'time'
		if sort:
			if sort == 'time':
				items = items.order_by('-id')
			elif sort == 'time-rev':
				items = items.order_by('id')
				selected_order = 'time-rev'
			elif sort == 'price':
				items = items.order_by('price')
				selected_order = 'price'
			elif sort == 'price-rev':
				items = items.order_by('-price')
				selected_order = 'price-rev'

		return render( request, self.template_name, { 'items':items, 'category_list':category_list, 'selected_order': selected_order, 'cats':Item.CATEGORIES })


class SellerProfile(TemplateView):
	template_name = 'shop/seller.html'

	def get( self, request, seller ):
		items = Item.objects.filter(user=seller).order_by('-id')
		return render(request, self.template_name, {'items':items})
