from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # Includes all URLs starting with /api/
    # path('users/', include('users.urls')), # If you add user URLs later
]
