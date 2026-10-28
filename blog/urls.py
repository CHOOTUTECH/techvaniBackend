from django.urls import path, include
from django.contrib.sitemaps.views import sitemap  # ✅ यह इम्पोर्ट ज़रूरी है
from rest_framework.routers import DefaultRouter
from blog.sitemaps import ArticleSitemap, HomepageSitemap
from .views import (
    ArticleViewSet, CategoryViewSet, TagViewSet, AuthorViewSet,
    StaticPageViewSet, NewsletterSubscribeView
)

sitemaps = {
    "homepage": HomepageSitemap(),
    "articles": ArticleSitemap(),
}

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'pages', StaticPageViewSet, basename='static-page')

urlpatterns = [
    # ✅ साइटमैप सर्व करने वाला रूट
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

    path('newsletter/subscribe/', NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
    path('', include(router.urls)),
]