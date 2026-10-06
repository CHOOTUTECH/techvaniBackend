from django.db import models
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Author, Tag, Article, StaticPage, Comment, NewsletterSubscriber
from .serializers import (
    CategorySerializer, AuthorSerializer, TagSerializer,
    ArticleSerializer, ArticleListSerializer, StaticPageSerializer, CommentSerializer,
    NewsletterSerializer
)

class ArticleFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='iexact')
    tag = django_filters.CharFilter(field_name='tags__slug', lookup_expr='iexact')

    class Meta:
        model = Article
        fields = ['category', 'category__slug', 'tag', 'tags__slug', 'sub_category', 'is_featured', 'is_trending']

class ArticleViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Articles:
    - GET /api/v1/articles/
    - POST /api/v1/articles/ (Create from Admin)
    - GET /api/v1/articles/{slug}/
    - PUT/PATCH /api/v1/articles/{slug}/ (Update)
    - DELETE /api/v1/articles/{slug}/
    """
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ArticleFilter
    search_fields = ['title', 'excerpt', 'content', 'meta_title', 'keywords', 'category__name']
    ordering_fields = ['views_count', 'published_at', 'rating', 'reading_time_minutes']
    ordering = ['-published_at']

    def get_serializer_class(self):
        # 🚀 Use lightweight serializer for lists and trending (skips heavy content body)
        if self.action in ['list', 'trending']:
            return ArticleListSerializer
        return ArticleSerializer

    def get_queryset(self):
        qs = Article.objects.filter(is_published=True).select_related('category', 'author').prefetch_related('tags')
        # 🚀 CRUCIAL: Do not fetch heavy 'content' column across the internet for list views
        if self.action in ['list', 'trending']:
            return qs.defer('content')
        return qs

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Atomic views increment without locking
        Article.objects.filter(pk=instance.pk).update(views_count=models.F('views_count') + 1)
        instance.views_count += 1
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def trending(self, request):
        limit = int(request.query_params.get('limit', 5))
        # Eliminates N+1 query overhead for remote databases like Supabase
        trending = (
            self.get_queryset()
            .order_by('-views_count')[:limit]
        )
        serializer = self.get_serializer(trending, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, slug=None):
        identifier = slug or self.kwargs.get('slug')
        if str(identifier).isdigit():
            article = Article.objects.filter(pk=int(identifier)).first()
        else:
            article = Article.objects.filter(slug=identifier).first()

        if not article:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'POST':
            author_name = request.data.get('authorName') or request.data.get('author_name', '')
            author_email = request.data.get('authorEmail') or request.data.get('author_email', '')
            comment_text = request.data.get('comment', '')

            if not author_name or not comment_text:
                return Response({'error': 'Name and comment are required'}, status=status.HTTP_400_BAD_REQUEST)

            comment = Comment.objects.create(
                article=article,
                author_name=author_name,
                author_email=author_email,
                comment=comment_text,
                is_approved=True
            )
            Article.objects.filter(pk=article.pk).update(comments_count=models.F('comments_count') + 1)

            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        comments = article.comments.filter(is_approved=True).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    lookup_field = 'slug'


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
    lookup_field = 'slug'


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = None


class StaticPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer
    lookup_field = 'slug'


class NewsletterSubscribeView(APIView):
    def post(self, request):
        email = request.data.get('email', '').strip().lower()
        if not email or '@' not in email:
            return Response({'success': False, 'message': 'कृपया एक मान्य ईमेल दर्ज करें।'}, status=status.HTTP_400_BAD_REQUEST)

        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
        if not created and not subscriber.is_active:
            subscriber.is_active = True
            subscriber.save()

        return Response({
            'success': True,
            'message': 'बधाई हो! आप सफलतापूर्वक टेकवाणी न्यूज़लेटर से जुड़ चुके हैं।'
        }, status=status.HTTP_200_OK)
