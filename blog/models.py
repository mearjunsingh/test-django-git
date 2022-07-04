from django.db import models


class Post(models.Model):
    # id = models.IntegerField(primary_key=True, null=False, blank=False)

    CAT_CHOICES = (
        ("sport", "Sport News"),
        ("news", "News"),
        ("pol", "Politics"),
    )

    title = models.CharField(
        max_length=254, null=False, blank=False, verbose_name="post title"
    )
    thumbnail = models.ImageField("post thumbnail", upload_to="posts/", blank=True)
    summary = models.CharField(max_length=400, null=True, blank=True)
    content = models.TextField(verbose_name="post content", null=True, blank=True)
    views = models.IntegerField("post views", default=0)
    is_published = models.BooleanField("post is published", default=True)
    category = models.CharField("post category", max_length=30, choices=CAT_CHOICES)
    created_at = models.DateField(verbose_name="created at", auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"
