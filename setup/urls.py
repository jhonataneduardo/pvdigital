from .views import index
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from knox import views as knox_views

from accounts.views.user import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, UserMe
from accounts.views.auth import LoginAPI

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/v1/auth/login/', LoginAPI.as_view(), name='login'),
    path('api/v1/auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/v1/auth/logoutall/',
         knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/v1/auth/me/', UserMe.as_view(), name='get_user_me'),
    path('api/v1/auth/users/', UserListCreateAPIView.as_view(),
         name='list_create_user'),
    path('api/v1/auth/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(),
         name='get_update_delete_user'),
    path('api/', include('base.urls')),
    path('api/', include('school.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
