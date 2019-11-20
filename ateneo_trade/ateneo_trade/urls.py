from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include('shop.urls')),
	path('admin/', admin.site.urls),
	path('account/', include('social_django.urls', namespace='social')),
	path('account/', include('django.contrib.auth.urls')),
]
