from django.urls import path, include
from base.views.person import (
    PersonListCreateAPIView, PersonRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('v1/persons/', PersonListCreateAPIView.as_view(), name='list_create_person'),
    path('v1/persons/<int:pk>/', PersonRetrieveUpdateDestroyAPIView.as_view(), name='get_update_delete_person'),
]