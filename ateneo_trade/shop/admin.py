from django.contrib import admin

# Register your models here.
from shop.models import *

admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Image)
