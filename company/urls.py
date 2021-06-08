from django.urls import path
from company.views.company import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(
        'companies/',
        CompanyListCreateAPIView.as_view(),
        name='list_create_company'),
    path(
        'companies/<int:pk>/',
        CompanyRetrieveUpdateDestroyAPIView.as_view(),
        name='get_update_delete_company'),
]
