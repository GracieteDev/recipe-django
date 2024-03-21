from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "meal_type",
        "cuisine_types",
        "instructions",
        "ingredients",
        "calories",
        "image",
    )
    list_filter = ("meal_type",)


