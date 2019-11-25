from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 
from . import views

urlpatterns = [
    path('', login_required(views.Home.as_view()), name='home'),
    # path('profile/', views.update_profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.post_item, name='post_item'),
    path('account/logout/', views.Logout, name='logout'),
    path('item/<int:id>/detail/', login_required(views.ViewItemDetail.as_view()), name='view-item-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
