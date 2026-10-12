from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Article.objects.filter(is_published=True)

    def location(self, obj):
        return f"/blog/{obj.slug}/"

    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(
            page=page,
            site=site,
            protocol="https",
        )
        for url in urls:
            url["location"] = (
                "https://localfinder.shop" + url["location"]
            )
        return urls

    def lastmod(self, obj):
        return getattr(obj, "updated_at", None)