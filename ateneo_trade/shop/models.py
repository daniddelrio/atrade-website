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
	major = models.CharField(max_length=10,null=False,blank=True,default="")
	trade_pts = models.IntegerField(default=0,null=False);
	contact_num = models.CharField(max_length=11,null=False,blank=False,default="00000000000");
	fb_link = models.CharField(max_length=40,null=False,blank=False,default="facebook.com/<your_profile>");
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()