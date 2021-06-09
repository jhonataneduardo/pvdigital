from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        'api/v1/',
        include('accounts.urls'), name='account_url'),
    path(
        'api/v1/',
        include('company.urls'), name='company_url'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
