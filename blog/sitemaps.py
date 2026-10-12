
from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Article.objects.filter(is_published=True)

    def location(self, obj):
        return f"/blog/{obj.slug}/"

    def lastmod(self, obj):
        return getattr(obj, "updated_at", None)
