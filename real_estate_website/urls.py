from django.urls import path
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),  # مسیر صفحه اصلی
]

# افزودن مسیر فایل‌های رسانه‌ای
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    