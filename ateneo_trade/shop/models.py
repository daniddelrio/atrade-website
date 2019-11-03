from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Profile(models.Model):
	user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
	school = models.TextField(max_length=4,blank=True)
	grad_year = models.IntegerField(validators=[MinValueValidator(1859), MaxValueValidator(9999)], default=datetime.date.today().year,blank=True)
	course = models.IntegerField(max_length=10,null=False,blank=True,default="")
	trade_pts = models.IntegerField(default=0);
	contact_num = models.IntegerField(null=False,blank=False);
	fb_link = models.CharField(null=False,blank=False);
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()