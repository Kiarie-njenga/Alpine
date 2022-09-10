from django.urls import path
from .import views









urlpatterns = [
    path('create_request/', views.BuyersRequestCreateView.as_view(), name="create_request"),
    path('requests/<int:pk>/', views.BuyerRequestDetail.as_view(), name='request_detail'),
    path('requests/', views.BuyerRequestListView.as_view(), name='requests'),
    path('requests/<int:pk>/edit', views.BuyersRequestUpdateView.as_view(), name='request_edit'),
    path('requests/<int:pk>/delete', views.BuyerRequestDeleteView.as_view(), name='request_delete'),
    path('requests/<int:post_pk>/comments/<int:pk>/delete', views.CommentDeleteView.as_view(), name="comment_delete"),
    
    
]