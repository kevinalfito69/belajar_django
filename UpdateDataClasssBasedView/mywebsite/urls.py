from django.urls import path, include
from django.contrib import admin

urlpatterns = [
	path('sosmed/', include('sosmed.urls',namespace='sosmed')),
    path('admin/', admin.site.urls),
]
    