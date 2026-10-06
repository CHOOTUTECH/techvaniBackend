from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet, CategoryViewSet, TagViewSet, AuthorViewSet,
    StaticPageViewSet, NewsletterSubscribeView
)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'pages', StaticPageViewSet, basename='static-page')

urlpatterns = [
    path('newsletter/subscribe/', NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
    path('', include(router.urls)),
]
