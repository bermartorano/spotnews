# Generated by Django 4.2.3 on 2023-08-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]