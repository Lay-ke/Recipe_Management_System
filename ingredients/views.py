from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .models import Ingredient
from recipes.models import Recipe
from .serializers import IngredientSerializer, IngredientDetailSerializer
from recipes.serializers import RecipeListSerializer


class IngredientListCreateView(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        new_ingredient = request.data
        serializer = IngredientSerializer(data=new_ingredient)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ingredient created successfully.",
                             "Ingredient": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDetailUpdateDeleteView(APIView):
    def get(self, request, id):
        try:
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = IngredientDetailSerializer(ingredient)
        return Response(serializer.data)
    
    def put(self, request, id):
        try:
            update_ingredient = request.data
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = IngredientDetailSerializer(ingredient, data=update_ingredient)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update successful.",
                            "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response({"message": "Delete successful."}, status=status.HTTP_200_OK)
    

class IngredientRecipesView(APIView):
    def get(self, request, id):
        try:
            ingredient = Ingredient.objects.get(ingredient_id=id)
        except Ingredient.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        recipes = Recipe.objects.filter(ingredients=ingredient) # consider indexing the ingredient_id and optimizing the query
        if not recipes.exists():
            return Response({"detail": "No recipes found for this ingredient."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)