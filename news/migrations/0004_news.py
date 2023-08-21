# Generated by Django 4.2.3 on 2023-08-21 20:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(1)
                        ],
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        validators=[
                            django.core.validators.MinLengthValidator(1)
                        ]
                    ),
                ),
                ("created_at", models.DateField()),
                ("image", models.ImageField(null=True, upload_to="img/")),
                (
                    "author",
                    models.ForeignKey(
                        default=2,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="news",
                        to="news.users",
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="news", to="news.categories"
                    ),
                ),
            ],
        ),
    ]
