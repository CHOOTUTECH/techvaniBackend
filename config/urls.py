from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import ArticleSitemap

sitemaps = {
    "articles": ArticleSitemap(),
}

# Customize Django Admin Header and Title in Hindi
admin.site.site_header = "टेकवाणी (TechVani) - मुख्य संपादक और एडमिन पैनल"
admin.site.site_title = "TechVani Admin Portal"
admin.site.index_title = "ब्लॉग पोस्ट्स, SEO मेटा और सामग्री प्रबंधन"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
