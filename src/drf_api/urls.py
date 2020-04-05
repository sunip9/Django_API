
from django.contrib import admin
from django.urls import path, include
from core.views import TestView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain_token'),
    path('', TestView.as_view(), name='test')
]
