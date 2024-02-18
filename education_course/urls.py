from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/materials/', include('materials.urls')),
    path('api/members/', include('members.urls')),
]
