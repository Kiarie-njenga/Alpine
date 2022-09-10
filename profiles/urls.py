from django.urls import path
from . import views






app_name='profiles'

urlpatterns=[
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', views.ProfileEditView.as_view(), name="profile_edit"),
    path('profiles/<int:pk>/order_detail/', views.get_ordered_items, name="profile_order_detail"),
    path('profile/sent_orders/', views.get_sent_items, name='sent_orders'),
 
]