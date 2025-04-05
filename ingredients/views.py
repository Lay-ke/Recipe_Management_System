from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .models import Ingredient
from recipes.models import Recipe
from .serializers import IngredientSerializer
from recipes.serializers import RecipeSerializer


class IngredientListCreateView(APIView):
    # Handles listing all ingredients and creating a new ingredient
    def get(self, request):
        # Retrieve all ingredients and serialize them
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Create a new ingredient from request data
        new_ingredient = request.data
        serializer = IngredientSerializer(data=new_ingredient)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ingredient created successfully.",
                             "Ingredient": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDetailUpdateDeleteView(APIView):
    # Handles retrieving, updating, and deleting a specific ingredient by ID
    def get(self, request, id):
        # Retrieve a specific ingredient by ID
        try:
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)
    
    def put(self, request, id):
        # Update a specific ingredient by ID
        try:
            update_ingredient = request.data
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = IngredientSerializer(ingredient, data=update_ingredient)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update successful.",
                            "Ingredient": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        # Delete a specific ingredient by ID
        try:
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response({"message": "Delete successful."}, status=status.HTTP_200_OK)
    

class IngredientRecipesView(APIView):
    # Handles retrieving all recipes that use a specific ingredient
    def get(self, request, id):
        # Retrieve a specific ingredient by ID
        try:
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve recipes that include the ingredient
        recipes = Recipe.objects.filter(ingredients=ingredient)  # Consider indexing ingredient_id for optimization
        if not recipes.exists():
            return Response({"detail": "No recipes found for this ingredient."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)