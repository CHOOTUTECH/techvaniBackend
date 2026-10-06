from rest_framework import serializers
from .models import Category, Author, Tag, Article, StaticPage, Comment, NewsletterSubscriber

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'icon', 'meta_title', 'meta_description']


class AuthorSerializer(serializers.ModelSerializer):
    articlesCount = serializers.IntegerField(source='articles_count', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'role', 'avatar', 'bio', 'twitter', 'articlesCount']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    authorName = serializers.CharField(source='author_name')
    authorEmail = serializers.EmailField(source='author_email', required=False, allow_blank=True)
    createdAt = serializers.DateTimeField(source='created_at', format='%d %B %Y, %I:%M %p', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'authorName', 'authorEmail', 'comment', 'createdAt']


class ArticleListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for listing articles without transferring
    heavy 'content' TextField over network. Speeds up API by 10x!
    """
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    # CamelCase mapping for smooth frontend compatibility
    coverImage = serializers.CharField(source='cover_image')
    imageAlt = serializers.CharField(source='image_alt')
    subCategory = serializers.CharField(source='sub_category', required=False, allow_blank=True)
    readingTimeMinutes = serializers.IntegerField(source='reading_time_minutes')
    viewsCount = serializers.IntegerField(source='views_count')
    commentsCount = serializers.IntegerField(source='comments_count')
    publishedAt = serializers.DateTimeField(source='published_at', format='%d %B %Y', read_only=True)
    isFeatured = serializers.BooleanField(source='is_featured', default=False)
    isEditorialChoice = serializers.BooleanField(source='is_editorial_choice', read_only=True)
    isTrending = serializers.BooleanField(source='is_trending', read_only=True)
    featuredOrder = serializers.IntegerField(source='featured_order', read_only=True)
    videoDuration = serializers.CharField(source='video_duration', read_only=True)
    productPrice = serializers.CharField(source='product_price', read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'excerpt', 'coverImage', 'imageAlt',
            'category', 'subCategory', 'author', 'tags',
            'readingTimeMinutes', 'viewsCount', 'commentsCount', 'publishedAt',
            'isFeatured', 'is_featured', 'isEditorialChoice', 'isTrending', 'featuredOrder', 'rating',
            'productPrice', 'videoDuration'
        ]


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    # CamelCase mapping for smooth frontend compatibility
    coverImage = serializers.CharField(source='cover_image')
    imageAlt = serializers.CharField(source='image_alt')
    subCategory = serializers.CharField(source='sub_category', required=False, allow_blank=True)
    readingTimeMinutes = serializers.IntegerField(source='reading_time_minutes')
    viewsCount = serializers.IntegerField(source='views_count')
    commentsCount = serializers.IntegerField(source='comments_count')
    publishedAt = serializers.DateTimeField(source='published_at', format='%d %B %Y', read_only=True)
    isFeatured = serializers.BooleanField(source='is_featured', default=False)
    isEditorialChoice = serializers.BooleanField(source='is_editorial_choice', read_only=True)
    isTrending = serializers.BooleanField(source='is_trending', read_only=True)
    featuredOrder = serializers.IntegerField(source='featured_order', read_only=True)
    videoDuration = serializers.CharField(source='video_duration', read_only=True)
    productPrice = serializers.CharField(source='product_price', read_only=True)

    # SEO & Google SERP Fields
    metaTitle = serializers.CharField(source='meta_title', required=False, allow_blank=True)
    metaDescription = serializers.CharField(source='meta_description', required=False, allow_blank=True)
    canonicalUrl = serializers.CharField(source='canonical_url', required=False, allow_blank=True)
    ogImage = serializers.CharField(source='og_image', required=False, allow_blank=True)
    schemaType = serializers.CharField(source='schema_type', required=False)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'excerpt', 'content', 'coverImage', 'imageAlt',
            'category', 'subCategory', 'author', 'tags',
            'readingTimeMinutes', 'viewsCount', 'commentsCount', 'publishedAt',
            'isFeatured', 'is_featured', 'isEditorialChoice', 'isTrending', 'featuredOrder', 'rating',
            'productPrice', 'videoDuration',
            'metaTitle', 'metaDescription', 'canonicalUrl', 'ogImage', 'schemaType'
        ]


class StaticPageSerializer(serializers.ModelSerializer):
    metaTitle = serializers.CharField(source='meta_title', required=False, allow_blank=True)
    metaDescription = serializers.CharField(source='meta_description', required=False, allow_blank=True)

    class Meta:
        model = StaticPage
        fields = ['id', 'title', 'slug', 'content', 'metaTitle', 'metaDescription', 'updated_at']


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
