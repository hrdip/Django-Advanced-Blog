# Generated by Django 3.2.23 on 2023-11-24 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
                ("description", models.TextField()),
                ("bio", models.TextField()),
                ("facebook_profile", models.URLField(blank=True, null=True)),
                ("instagram_profile", models.URLField(blank=True, null=True)),
                ("linkedin_profile", models.URLField(blank=True, null=True)),
                ("created_date", models.DateField(auto_now_add=True)),
                ("updated_date", models.DateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
