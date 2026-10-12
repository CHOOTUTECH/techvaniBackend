from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Article.objects.filter(is_published=True)

    def location(self, obj):
        return f"https://localfinder.shop/blog/{obj.slug}/"

    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(
            page=page,
            site=site,
            protocol="https",
        )

        for url in urls:
            url["location"] = (
                f"https://localfinder.shop/blog/{url['item'].slug}/"
            )

        return urls