from django.db import models


class Post(models.Model):
    # id = models.IntegerField(primary_key=True, null=False, blank=False)
    title = models.CharField(
        max_length=254, null=False, blank=False, verbose_name="post title"
    )
    summary = models.CharField(max_length=400, null=False, blank=False)
    content = models.TextField(verbose_name="post content", null=False, blank=False)
    created_at = models.DateField(verbose_name="created at", auto_now_add=True)
