from django.db import models
from django.urls import reverse

from .utils import generate_new_slug


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    title = models.CharField(
        max_length=254, null=False, blank=False, verbose_name="post title"
    )
    slug = models.SlugField(unique=True, null=False, blank=False, editable=False)
    thumbnail = models.ImageField("post thumbnail", upload_to="posts/", blank=True)
    summary = models.CharField(max_length=400, null=True, blank=True)
    content = models.TextField(verbose_name="post content", null=True, blank=True)
    views = models.IntegerField("post views", default=0)
    is_published = models.BooleanField("post is published", default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="created at", auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    def save(self, *args, **kwargs):
        self.slug = generate_new_slug(Post, self.title)
        return super().save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse("single_blog_page", args=[self.slug])
