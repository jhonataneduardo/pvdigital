from django.urls import path, include
from knox import views as knox_views

from accounts.views.user import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from accounts.views.auth import LoginAPI

urlpatterns = [
    path(
        'login/',
        LoginAPI.as_view(),
        name='login'),
    path(
        'logout/',
        knox_views.LogoutView.as_view(),
        name='logout'),
    path(
        'logoutall/',
        knox_views.LogoutAllView.as_view(),
        name='logoutall'),
    path(
        'users/',
        UserListCreateAPIView.as_view(),
        name='list_create_user'),
    path(
        'users/<int:pk>/',
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name='get_update_delete_user'),
]
