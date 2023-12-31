# Generated by Django 4.2.3 on 2023-08-21 21:18

from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0006_alter_news_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(
                validators=[news.validators.word_count_validator]
            ),
        ),
    ]
