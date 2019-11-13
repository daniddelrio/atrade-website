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
	user = models.OneToOneField(User, db_index=True, null=False, on_delete=models.CASCADE, unique=True)
	school = models.CharField(blank=True, max_length=4)
	grad_year = models.IntegerField(blank=True, default=datetime.date.today().year, validators=[MinValueValidator(1859), MaxValueValidator(9999)])
	major = models.CharField(blank=True, default="", help_text="Please use the following format: BS CS", max_length=10, null=False)
	trade_pts = models.IntegerField(default=0, null=False);
	contact_num = models.CharField(blank=False, default="", help_text="Please use the following format: +639123456789", max_length=11, null=False);
	fb_link = models.CharField(blank=False, default="", help_text="Please use the following format: facebook.com/your.profile", max_length=40, null=False);
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Item(models.Model):
	user = models.ForeignKey(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
	price = DecimalField(max_digits=11,decimal_places=2,null=False, blank=False)
	description = models.TextField(null=False,blank=False)