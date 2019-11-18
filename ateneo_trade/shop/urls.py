from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('profile/', views.update_profile, name='profile'),
    path('account/logout/', views.Logout, name='logout'),
    path('item/post/', views.post_item, name='post_item'),
]
