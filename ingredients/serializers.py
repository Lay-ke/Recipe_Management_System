from rest_framework import serializers
from .models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredient_id', 'name', 'description']
        read_only_fields = ['ingredient_id']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False, 'allow_blank': True}
        }

    
class IngredientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredient_id', 'name', 'description']
        read_only_fields = ['ingredient_id']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False, 'allow_blank': True}
        }
        depth = 1

