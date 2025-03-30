from rest_framework import serializers
from .models import Recipe, RecipeIngredient

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_id = serializers.PrimaryKeyRelatedField(queryset=RecipeIngredient.objects.all())

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient_id', 'unit', 'quantity']


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['recipe_id', 'title', 'description', 'ingredients', 'instructions', 'cook_time', 'prep_time', 'phote', 'difficulty', 'servings', 'user_id', 'category_id']
        read_only_fields = ['recipe_id', 'created_at']
        extra_kwargs = {
            'user_id': {'required': True},
            'phote': {'required': False},
            'cook_time': {'required': True},
            'servings': {'required': True}
        }

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            RecipeIngredient.objects.create(recipe_id=recipe, **ingredient_data)
        return recipe


class RecipeUpdateSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'cook_time', 'prep_time', 'phote', 'difficulty', 'servings', 'category_id']
        extra_kwargs = {
            'phote': {'required': False},
            'cook_time': {'required': True},
            'servings': {'required': True}
        }

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        instance = super().update(instance, validated_data)

        # Clear existing ingredients and add updated ones
        instance.ingredients.all().delete()
        for ingredient_data in ingredients_data:
            RecipeIngredient.objects.create(recipe_id=instance, **ingredient_data)
        return instance


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['recipe_id', 'title', 'description', 'cook_time', 'prep_time', 'difficulty', 'servings', 'category_id']


# class RecipeDeleteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = ['recipe_id']
    

# class RecipeDetailSerializer(serializers.ModelSerializer):
#     ingredients = RecipeIngredientSerializer(many=True)
    
#     class Meta:
#         model = Recipe
#         fields = ['recipe_id', 'title', 'description', 'ingredients', 'instructions', 'cook_time', 'prep_time', 'phote', 'difficulty', 'servings', 'user_id', 'category_id', 'created_at']
#         read_only_fields = ['recipe_id', 'created_at']
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         # Add any additional data validation or transformation here if needed
#         return representation