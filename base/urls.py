from django.urls import path
from base.views.person import PersonListCreateAPIView, PersonRetrieveUpdateDestroyAPIView
from base.views.company import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView
from base.views.employee import EmployeeCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('v1/persons/', PersonListCreateAPIView.as_view(),
         name='list_create_person'),
    path('v1/persons/<int:pk>/', PersonRetrieveUpdateDestroyAPIView.as_view(),
         name='get_update_delete_person'),

    path('v1/companies/', CompanyListCreateAPIView.as_view(),
         name='list_create_company'),
    path('v1/companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(),
         name='get_update_delete_company'),

    path('v1/employees/', EmployeeCreateAPIView.as_view(),
         name='list_create_employee'),
    path('v1/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(),
         name='get_update_delete_employee'),
]
