from .models import Category 
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description', 'created_at', 'updated_at']  # Adjust fields as per your model


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description', 'created_at', 'updated_at']  # Adjust fields as per your model


# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = ['id', 'title', 'description', 'ingredients', 'instructions']  # Adjust fields as per your model
