from django.urls import path, include
from . import views

urlpatterns = [
    # path('', include('shop.urls'))
    path('', views.index, name='index')
]
