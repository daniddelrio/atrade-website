from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

def user_directory_path(instance):
	return 'user_{0}/'.format(instance.user.id)

class Profile(models.Model):
	SCHOOL_CHOICES = [
		('SOSE', 'SOSE'),
		('SOM', 'SOM'),
		('SOSS', 'SOSS'),
		('SOH', 'SOH'),
	]
	user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE, unique=True)
	school = models.CharField(blank=True, choices=SCHOOL_CHOICES, default=None, max_length=4, null=True)
	school_is_visible = models.BooleanField(default=False)
	grad_year = models.IntegerField(blank=True, default=None, null=True, validators=[MinValueValidator(1859), MaxValueValidator(9999)])
	gradyr_is_visible = models.BooleanField(default=False)
	major = models.CharField(blank=True, default=None, help_text="Please use the following format: BS CS", max_length=10, null=True)
	major_is_visible = models.BooleanField(default=False)
	trade_pts = models.IntegerField(default=0)
	contact_num = models.CharField(default="", help_text="Please use the following format: +639123456789", max_length=15)
	fb_link = models.CharField(default="facebook.com", help_text="Please use the following format: facebook.com/your.profile", max_length=40)

class DisplayPicture(models.Model):
	user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE, unique=True)
	display_pic = models.ImageField(default="default-user.jpg", upload_to=user_directory_path)	

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Item(models.Model):
	CATEGORIES = [
		('Academic Books', 'Academic Books'),
		('Non-Academic Books', 'Non-Academic Books'),
		('School Supplies', 'School Supplies'),
		('Clothes', 'Clothes'),
	]
	user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
	name = models.CharField(default="", max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=11)
	description = models.TextField(default="")
	category = models.CharField(choices=CATEGORIES, default="", max_length=100)
	location = models.CharField(default="Ateneo de Manila University", max_length=200)
	is_sold = models.BooleanField(default=False)

class Image(models.Model):
	item = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/%Y/%m/%d/')

class Rating(models.Model):
	rater = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE, related_name='user_rater')
	ratee = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE, related_name='user_ratee')
	rating_number = models.IntegerField(blank=True, null=True)
