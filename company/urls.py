from django.urls import path
from company.views.company import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView
from company.views.employee import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(
        'companies/',
        CompanyListCreateAPIView.as_view(),
        name='list_create_company'),
    path(
        'companies/<int:pk>/',
        CompanyRetrieveUpdateDestroyAPIView.as_view(),
        name='get_update_delete_company'),
    path(
        'employees/',
        EmployeeListCreateAPIView.as_view(),
        name='list_create_employee'),
    path(
        'employees/<int:pk>/',
        EmployeeRetrieveUpdateDestroyAPIView.as_view(),
        name='get_update_delete_employee'),
]
