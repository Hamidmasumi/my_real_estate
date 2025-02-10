from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('real_estate_website.urls')),  # اتصال به فایل urls.py داخل real_estate_website
]