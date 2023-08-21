from django.db import models
from .user_model import Users
from ..validators import word_count_validator


class News(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        validators=[word_count_validator]
    )
    content = models.TextField(
        null=False,
        blank=False,
        )
    created_at = models.DateField(
        null=False,
        blank=False,
    )
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="news",
        default=2,
    )
    categories = models.ManyToManyField(
        "Categories",
        related_name="news",
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title
