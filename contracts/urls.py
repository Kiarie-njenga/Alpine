







from django.urls import path
from . import views






app_name='contract'

urlpatterns=[
    path('list', views.ContractListView.as_view(), name='contract_list'),
    path('search', views.ContractSearch.as_view(), name='contract_search'),
    path('contracts/create/', views.ContractCreateView.as_view(), name="create_contract"),
    path('contracts/<int:pk>/edit', views.ContractEditView.as_view(), name="edit_contract"),
    path('contracts/<int:pk>/delete', views.ContractDeleteView.as_view(), name="delete_contract"),
    path('contracts/<int:pk>/', views.ContractDetailView.as_view(), name='contract_detail'),
    
]