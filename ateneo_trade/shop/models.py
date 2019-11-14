from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Profile(models.Model):
	SCHOOL_CHOICES = [
		('SOSE', 'SOSE'),
		('SOM', 'SOM'),
		('SOSS', 'SOSS'),
		('SOH', 'SOH'),
	]
	user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE, unique=True)
	school = models.CharField(blank=True, choices=SCHOOL_CHOICES, default=None, max_length=4, null=True)
	grad_year = models.IntegerField(blank=True, default=None, null=True, validators=[MinValueValidator(1859), MaxValueValidator(9999)])
	major = models.CharField(blank=True, default=None, help_text="Please use the following format: BS CS", max_length=10, null=True)
	trade_pts = models.IntegerField(default=0);
	contact_num = models.CharField(default="", help_text="Please use the following format: +639123456789", max_length=11);
	fb_link = models.CharField(default="", help_text="Please use the following format: facebook.com/your.profile", max_length=40);
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

# TODO: add image uploading
class Item(models.Model):
	CATEGORIES = [
		('academic_books', 'Academic Books'),
		('nacademic_books', 'Non-Academic Books'),
		('school_supplies', 'School Supplies'),
		('clothes', 'Clothes'),
	]
	user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
	name = models.CharField(default="", max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=11)
	description = models.TextField(default="")
	category = models.CharField(choices=CATEGORIES, default="", max_length=100)
	location = models.CharField(default="Ateneo de Manila University", max_length=200)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Image(models.Model):
	item_id = models.ForeignKey(Item)
	image = models.ImageField(upload_to=user_directory_path)
	