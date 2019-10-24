from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('shop.urls'))
	# url(r'^', include('home.urls')),
	url(r'^account/', include('social_django.urls', namespace='social')),
	url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),
]
