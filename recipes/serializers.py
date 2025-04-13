from rest_framework import serializers
from .models import Recipe, RecipeIngredient
from ingredients.models import Ingredient

class RecipeIngredientSerializer(serializers.ModelSerializer):
    # Using a PK related field for writing, but on output it will be part of the nested representation.
    ingredient_id = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    unit = serializers.CharField(max_length=100)
    quantity = serializers.CharField(max_length=100)

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient_id', 'unit', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    # For creation, we expect a list of ingredients with unit and quantity.
    ingredients = RecipeIngredientSerializer(many=True, write_only=True)

    class Meta:
        model = Recipe
        # Using all fields; the ones below are read-only.
        fields = '__all__'
        read_only_fields = ['recipe_id', 'created_at']

        extra_kwargs = {
            'user_id': {'required': True},
            'category_id': {'required': True},
            'title': {'required': True},
            'description': {'required': True},
            'instructions': {'required': True},
            'prep_time': {'required': True},
            'cook_time': {'required': True},
            'servings': {'required': True},
            'difficulty': {'required': True},
            'phote': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        # Pop out the ingredients data that comes from the nested field.
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)

        # Create the through model entries (RecipeIngredient) for each ingredient.
        for ingredient_data in ingredients_data:
            ingredient = ingredient_data.pop('ingredient_id')
            RecipeIngredient.objects.create(
                recipe_id=recipe,
                ingredient_id=ingredient,
                **ingredient_data
            )
        return recipe
    
    def update(self, instance, validated_data):
        # Extract ingredients data from the update payload.
        ingredients_data = validated_data.pop('ingredients', None)

        # Update the recipe instance with any new values.
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if ingredients_data is not None:
            # Clear out the old RecipeIngredient entries.
            instance.recipeingredient_set.all().delete()
            # Re-create RecipeIngredient entries based on the new list.
            for ingredient_data in ingredients_data:
                ingredient = ingredient_data.pop('ingredient_id')
                RecipeIngredient.objects.create(
                    recipe_id=instance,
                    ingredient_id=ingredient,
                    **ingredient_data
                )
        return instance

    def to_representation(self, instance):
        # Get the default representation first.
        rep = super().to_representation(instance)
        # Replace the "ingredients" field with nested details from RecipeIngredient.
        recipe_ingredients = RecipeIngredient.objects.filter(recipe_id=instance)
        rep['ingredients'] = RecipeIngredientSerializer(recipe_ingredients, many=True).data
        return rep


            
      