from django.contrib.sitemaps import Sitemap
from .models import Article

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Article.objects.filter(is_published=True)

    def location(self, obj):
        # ✅ blog की जगह article
        return f"https://www.techvani.co.in/article/{obj.slug}"

    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(page=page, site=site, protocol="https")
        for url in urls:
            # ✅ blog की जगह article
            url["location"] = f"https://www.techvani.co.in/article/{url['item'].slug}"
        return urls


class HomepageSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = "https"

    def items(self):
        return ['home']

    def location(self, item):
        return "https://www.techvani.co.in/"