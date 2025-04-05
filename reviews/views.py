from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Review
from recipes.models import Recipe
from .serializers import ReviewSerializer

# This view handles the creation and retrieval of reviews for recipes.
# Its url pattern is defined in reviews/urls.py.
class ReviewListCreateView(APIView):
    # Get reviews for a recipe
    def get(self, request, recipe_id):
        """
        Retrieve all reviews for a specific recipe.
        """
        try:
            reviews = Review.objects.filter(recipe_id=recipe_id)
        except Review.DoesNotExist:
            return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create a review for a recipe
    def post(self, request, recipe_id):
        """
        Create a new review for a specific recipe.
        """
        try:
            # Fetch the Recipe instance using the recipe_id
            recipe = Recipe.objects.get(recipe_id=recipe_id)
        except Recipe.DoesNotExist:
            return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user, recipe_id=recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    # Update a review
    def put(self, request, review_id):
        """
        Update a review (owner only).
        """
        try:
            review = Review.objects.get(review_id=review_id, user_id=request.user)
        except Review.DoesNotExist:
            return Response({"detail": "Review not found or not owned by user"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a review
    def delete(self, request, review_id):
        """
        Delete a review (owner only).
        """
        try:
            review = Review.objects.get(review_id=review_id, user_id=request.user)
        except Review.DoesNotExist:
            return Response({"detail": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        review.delete
        return Response({"message": "Delete successful."}, status=status.HTTP_200_OK)