from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="श्रेणी का नाम (Category Name)")
    slug = models.SlugField(max_length=120, unique=True, blank=True, verbose_name="URL स्लग (Slug)")
    description = models.TextField(blank=True, verbose_name="श्रेणी विवरण (Description)")
    icon = models.CharField(max_length=50, default='terminal', verbose_name="आइकन नाम (Material Icon)")
    
    # SEO
    meta_title = models.CharField(max_length=255, blank=True, verbose_name="Google SEO Meta Title")
    meta_description = models.TextField(blank=True, verbose_name="Google SEO Meta Description")

    class Meta:
        verbose_name = "श्रेणी (Category)"
        verbose_name_plural = "श्रेणियां (Categories)"
        ordering = ['id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True) or f"category-{self.id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=120, verbose_name="लेखक का नाम (Author Name)")
    role = models.CharField(max_length=120, verbose_name="पद / विशेषज्ञता (Role)")
    avatar = models.URLField(max_length=500, verbose_name="प्रोफाइल फोटो URL (Avatar URL)")
    bio = models.TextField(verbose_name="संक्षिप्त परिचय (Bio)")
    twitter = models.CharField(max_length=100, blank=True, verbose_name="ट्विटर / X हैंडल")
    articles_count = models.PositiveIntegerField(default=0, verbose_name="प्रकाशित लेख संख्या")

    class Meta:
        verbose_name = "लेखक / संपादक (Author)"
        verbose_name_plural = "लेखक व संपादक टीम (Authors & Editorial Team)"

    def __str__(self):
        return f"{self.name} ({self.role})"


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="टैग नाम (Tag Name)")
    slug = models.SlugField(max_length=60, unique=True, blank=True, verbose_name="टैग स्लग (Slug)")

    class Meta:
        verbose_name = "टैग (Tag)"
        verbose_name_plural = "टैग्स (Tags)"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"#{self.name}"


class Article(models.Model):
    SCHEMA_CHOICES = [
        ('TechArticle', 'Tech Article (तकनीकी लेख)'),
        ('NewsArticle', 'News Article (समाचार)'),
        ('Product', 'Product Review (उत्पाद / गैजेट समीक्षा)'),
        ('HowTo', 'How-To Guide (कीबोर्ड शॉर्टकट / ट्यूटोरियल)'),
    ]

    # --- 1. मुख्य सामग्री (Main Blog Content) ---
    title = models.CharField(max_length=255, verbose_name="आर्टिकल का मुख्य शीर्षक (Title)")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL स्लग (Slug)")
    excerpt = models.TextField(verbose_name="संक्षिप्त सारांश (Excerpt/Summary)")
    content = models.TextField(verbose_name="विस्तृत लेख सामग्री (Article Content - Markdown or HTML)")
    cover_image = models.URLField(max_length=600, verbose_name="कवर फोटो URL (Cover Image URL)")
    image_alt = models.CharField(max_length=255, blank=True, default="TechVani Article Cover", verbose_name="इमेज Alt टेक्स्ट (SEO के लिए)")

    # --- 2. संबंध (Relationships) ---
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="मुख्य श्रेणी (Category)")
    sub_category = models.CharField(max_length=50, blank=True, verbose_name="सब-कैटेगरी / टैब (उदा: Python, Web Dev, टूलकिट)")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles', verbose_name="लेखक (Author)")
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles', verbose_name="टैग्स (Tags)")

    # --- 3. 🚀 SEO & GOOGLE SERP (Backend Managed) ---
    meta_title = models.CharField(
        max_length=255, 
        blank=True, 
        verbose_name="Google SEO Meta Title",
        help_text="गूगल सर्च में दिखने वाला शीर्षक। यदि खाली छोड़ेंगे तो मुख्य Title उपयोग होगा।"
    )
    meta_description = models.TextField(
        blank=True, 
        verbose_name="Google SEO Meta Description",
        help_text="गूगल सर्च स्निपेट (अनुशंसित: 120-160 अक्षर)। यदि खाली छोड़ेंगे तो Excerpt उपयोग होगा।"
    )
    canonical_url = models.URLField(
        blank=True, 
        verbose_name="Canonical URL",
        help_text="कैनोनिकल लिंक (सर्च इंजन में डुप्लिकेट कंटेंट से बचाव के लिए)।"
    )
    keywords = models.CharField(
        max_length=500, 
        blank=True, 
        verbose_name="Meta Keywords",
        help_text="कॉमा से अलग किए गए कीवर्ड्स (उदा: विंडोज 11, कीबोर्ड शॉर्टकट्स, एक्सेल)"
    )
    og_image = models.URLField(
        blank=True, 
        max_length=600,
        verbose_name="सोशल शेयर इमेज (OpenGraph Image)",
        help_text="फेसबुक / ट्विटर पर शेयर करते समय दिखने वाली इमेज (यदि खाली छोड़ेंगे तो Cover Image उपयोग होगी)।"
    )
    schema_type = models.CharField(
        max_length=50, 
        choices=SCHEMA_CHOICES, 
        default='TechArticle',
        verbose_name="Google Schema.org प्रकार (Schema Type)",
        help_text="गूगल रिच सर्च स्निपेट्स के लिए संरचित डेटा प्रकार।"
    )

    # --- 4. गैजेट व शॉर्टकट विवरण ---
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="समीक्षा रेटिंग / 10 (Review Rating)")
    product_price = models.CharField(max_length=100, blank=True, verbose_name="अनुमानित कीमत (उदा: ₹3,499)")
    video_duration = models.CharField(max_length=50, blank=True, verbose_name="वीडियो अवधि (उदा: 58 मिनट)")

    # --- 5. पब्लिश सेटिंग्स और मेट्रिक्स ---
    is_published = models.BooleanField(default=True, db_index=True, verbose_name="क्या प्रकाशित है? (Published)")
    is_featured = models.BooleanField(default=False, db_index=True, verbose_name="मुख्य फीचर लेख (Featured Article)")
    is_editorial_choice = models.BooleanField(default=False, db_index=True, verbose_name="संपादकीय पसंद (Editorial Choice)")
    is_trending = models.BooleanField(default=False, db_index=True, verbose_name="ट्रेंडिंग में दिखाएं (Trending)")
    featured_order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name="हीरो ग्रिड क्रम (0 = सामान्य, 1 = बड़ा हीरो, 2, 3 = साइड कार्ड्स)")
    
    reading_time_minutes = models.PositiveIntegerField(default=5, verbose_name="पढ़ने का समय (मिनट में)")
    views_count = models.PositiveIntegerField(default=0, db_index=True, verbose_name="व्यूज संख्या (Views Count)")
    comments_count = models.PositiveIntegerField(default=0, verbose_name="टिप्पणियां संख्या (Comments Count)")
    
    published_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="प्रकाशन तिथि (Published Date)")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="अंतिम संशोधन तिथि (Updated Date)")

    class Meta:
        verbose_name = "ब्लॉग पोस्ट / आर्टिकल (Article)"
        verbose_name_plural = "ब्लॉग पोस्ट्स (Articles)"
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True) or f"post-{self.id}"
        if not self.meta_title:
            self.meta_title = self.title
        if not self.meta_description:
            self.meta_description = self.excerpt[:160]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class StaticPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="पेज का शीर्षक (Title)")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL स्लग (उदा: about, privacy-policy)")
    content = models.TextField(verbose_name="पेज सामग्री (Content HTML/Text)")
    meta_title = models.CharField(max_length=255, blank=True, verbose_name="Google Meta Title")
    meta_description = models.TextField(blank=True, verbose_name="Google Meta Description")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="अंतिम अपडेट")

    class Meta:
        verbose_name = "स्टैटिक पेज (Static Policy/About Page)"
        verbose_name_plural = "पेज प्रबंधन (Pages: About, Privacy, Contact)"

    def __str__(self):
        return f"{self.title} (/{self.slug})"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="संबंधित आर्टिकल")
    author_name = models.CharField(max_length=120, verbose_name="पाठक का नाम")
    author_email = models.EmailField(blank=True, verbose_name="ईमेल पता")
    comment = models.TextField(verbose_name="टिप्पणी (Comment Text)")
    is_approved = models.BooleanField(default=True, verbose_name="क्या स्वीकृत है?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="दिनांक")

    class Meta:
        verbose_name = "टिप्पणी (Comment)"
        verbose_name_plural = "पाठकों की टिप्पणियां (Comments)"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author_name} - {self.article.title[:30]}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="ईमेल पता")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="सब्सक्रिप्शन तिथि")
    is_active = models.BooleanField(default=True, verbose_name="एक्टिव सदस्य")

    class Meta:
        verbose_name = "न्यूज़लेटर सब्सक्राइबर"
        verbose_name_plural = "न्यूज़लेटर ग्राहक सूची (Newsletter Subscribers)"

    def __str__(self):
        return self.email
