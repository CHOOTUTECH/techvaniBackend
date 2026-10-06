from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Customize Django Admin Header and Title in Hindi
admin.site.site_header = "टेकवाणी (TechVani) - मुख्य संपादक और एडमिन पैनल"
admin.site.site_title = "TechVani Admin Portal"
admin.site.index_title = "ब्लॉग पोस्ट्स, SEO मेटा और सामग्री प्रबंधन"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
