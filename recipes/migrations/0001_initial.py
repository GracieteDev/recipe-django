from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                ("title", models.CharField(max_length=300)),
                ("description", models.CharField(max_length=600)),
                (
                    "instructions",
                    djrichtextfield.models.RichTextField(max_length=15000),
                ),
                (
                    "ingredients",
                    djrichtextfield.models.RichTextField(max_length=10000),
                ),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[400, None],
                        upload_to="recipes/",
                    ),
                ),
                ("image_alt", models.CharField(max_length=100)),
                (
                    "meal_type",
                    models.CharField(
                        choices=[
                            ("breakfast", "Breakfast"),
                            ("lunch", "Lunch"),
                            ("dinner", "Dinner"),
                        ],
                        default="breakfast",
                        max_length=50,
                    ),
                ),
                (
                    "cuisine_types",
                    models.CharField(
                        choices=[
                            ("african", "African"),
                            ("south_american", "South American"),
                            ("asian", "Asian"),
                            ("middle_eastern", "Middle Eastern"),
                            ("indian", "Indian"),
                            ("european", "European"),
                            ("mediterranean", "Mediterranean"),
                        ],
                        default="african",
                        max_length=60,
                    ),
                ),
                ("calories", models.IntegerField()),
                ("posted_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipe_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-posted_date"],
            },
        ),
    ]
