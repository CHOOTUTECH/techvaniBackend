from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Author, Tag, Article, StaticPage, Comment, NewsletterSubscriber

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon', 'meta_title')
    search_fields = ('name', 'description', 'meta_title')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ("📁 श्रेणी विवरण", {
            'fields': ('name', 'slug', 'description', 'icon')
        }),
        ("🚀 श्रेणी SEO मेटाडेटा", {
            'fields': ('meta_title', 'meta_description'),
            'description': 'Google सर्च में इस श्रेणी का कस्टम टाइटल और डिस्क्रिप्शन।'
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'twitter', 'articles_count')
    search_fields = ('name', 'role', 'bio')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title_preview',
        'category',
        'author',
        'reading_time_minutes',
        'rating',
        'is_published',
        'is_featured_badge',
        'views_count',
        'published_at',
    )
    list_display_links = ('title_preview',)
    list_filter = (
        'category',
        'is_published',
        'is_featured',
        'is_editorial_choice',
        'is_trending',
        'schema_type',
        'published_at',
    )
    search_fields = ('title', 'excerpt', 'content', 'meta_title', 'keywords')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    list_editable = ('is_published',)
    list_per_page = 20
    date_hierarchy = 'published_at'

    # Rich Fieldsets for comfortable editing
    fieldsets = (
        ("📝 1. मुख्य लेख सामग्री (Main Article Content)", {
            'fields': (
                'title',
                'slug',
                'category',
                'sub_category',
                'author',
                'excerpt',
                'content',
                'cover_image',
                'image_alt',
                'tags',
            ),
            'description': 'यहाँ लेख का शीर्षक, विस्तृत सामग्री और कवर फोटो भरें। Markdown और HTML समर्थित है।'
        }),
        ("🚀 2. गूगल सर्च और SEO मेटाडेटा (Google SEO & Meta SERP)", {
            'fields': (
                'meta_title',
                'meta_description',
                'canonical_url',
                'keywords',
                'og_image',
                'schema_type',
            ),
            'description': 'Google Search और सोशल मीडिया पर दिखने वाला सटीक मेटा टाइटल और डिस्क्रिप्शन यहाँ से नियंत्रित करें।'
        }),
        ("⚙️ 3. उत्पाद समीक्षा और वीडियो विवरण (Review Specs & Duration)", {
            'fields': (
                'rating',
                'product_price',
                'video_duration',
            ),
            'classes': ('collapse',),
            'description': 'यदि यह हार्डवेयर समीक्षा या वीडियो ट्यूटोरियल है तो यहाँ रेटिंग या कीमत दर्ज करें।'
        }),
        ("📊 4. पब्लिश सेटिंग्स और प्लेसमेंट (Publish & Placement)", {
            'fields': (
                'is_published',
                'is_featured',
                'is_editorial_choice',
                'is_trending',
                'featured_order',
                'reading_time_minutes',
                'views_count',
            ),
        }),
    )

    def title_preview(self, obj):
        return format_html(
            '<strong>{}</strong><br/><span style="color:#888; font-size:11px;">/article/{}</span>',
            obj.title[:65] + '...' if len(obj.title) > 65 else obj.title,
            obj.slug
        )
    title_preview.short_description = "शीर्षक और स्लग"

    def is_featured_badge(self, obj):
        if obj.featured_order == 1:
            return format_html('<span style="color:#d9534f; font-weight:bold;">★ बड़ा हीरो</span>')
        elif obj.is_featured:
            return format_html('<span style="color:#0275d8;">★ फीचर्ड</span>')
        elif obj.is_trending:
            return format_html('<span style="color:#f0ad4e;">🔥 ट्रेंडिंग</span>')
        return "सामान्य"
    is_featured_badge.short_description = "प्लेसमेंट"


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'meta_title', 'updated_at')
    search_fields = ('title', 'content', 'meta_title')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ("📄 पेज विवरण", {
            'fields': ('title', 'slug', 'content')
        }),
        ("🚀 SEO मेटाडेटा", {
            'fields': ('meta_title', 'meta_description'),
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'article', 'comment_snippet', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('author_name', 'comment', 'article__title')
    list_editable = ('is_approved',)

    def comment_snippet(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    comment_snippet.short_description = "टिप्पणी"


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    search_fields = ('email',)
    list_filter = ('is_active', 'subscribed_at')
