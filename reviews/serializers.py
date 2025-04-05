from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'comment', 'rating', 'user_id', 'recipe_id', 'created_at']
        read_only_fields = ['review_id', 'created_at']
        extra_kwargs = {
            'user_id': {'required': True},
            'recipe_id': {'required': True},
        }