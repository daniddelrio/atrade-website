from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 
from . import views

urlpatterns = [
    path('', login_required(views.Home.as_view()), name='home'),
    path('categories/', login_required(views.Categories.as_view()), name='categories'),
    path('profile/', views.update_profile, name='profile'),
    path('your-items/', login_required(views.ViewYourItems.as_view()), name='your-items'),
    path('post/', views.post_item, name='post-item'),
    path('change-status/<int:pk>', views.change_status, name='change_status'),
    path('account/logout/', views.Logout, name='logout'),
    path('item/<int:id>/detail/', login_required(views.ViewItemDetail.as_view()), name='view-item-detail'),
    path('profile/seller/<int:seller>/', login_required(views.SellerProfile.as_view()), name='seller-profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
