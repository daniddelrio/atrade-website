from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
	school = models.TextField(max_length=4,blank=True)
	grad_year = models.IntegerField(validators=[alidators=[MinValueValidator(1859), MaxValueValidator(9999)]], default_value=current_year,blank=True)
	course = models.IntegerField(max_length=10,null=False,blank=True,default_value="")
	trade_pts = models.IntegerField();
	contact_num = models.IntegerField(null=False,blank=False);
	fb_link = models.CharField(null=False,blank=False);
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

def current_year():
    return datetime.date.today().year