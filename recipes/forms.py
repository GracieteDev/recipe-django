from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """
    A form to create and manage recipes
    """

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "instructions",
            "ingredients",
            "image",
            "image_alt",
            "meal_type",
            "cuisine_types",
            "calories",
        ]
        widgets = {
            "instructions": RichTextWidget(),
            "ingredients": RichTextWidget(),
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            "meal_type": "Meal Type",
            "cuisine_types": "Cuisine Type",
            "calories": "Calories",
        }
