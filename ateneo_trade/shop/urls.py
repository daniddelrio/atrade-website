from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home),
    path('profile/', views.update_profile),
    path('account/logout/', views.Logout),
]
