from django.urls import path, include
from knox import views as knox_views

from accounts.views.user import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from accounts.views.auth import LoginAPI

urlpatterns = [
    path('v1/auth/login/', LoginAPI.as_view(), name='login'),
    path('v1/auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('v1/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('v1/auth/users/', UserListCreateAPIView.as_view(), name='list_create_user'),
    path('v1/auth/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(),
         name='get_update_delete_user'),
]
