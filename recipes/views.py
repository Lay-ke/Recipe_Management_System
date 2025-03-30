from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializers import RecipeCreateSerializer, RecipeUpdateSerializer, RecipeListSerializer
# Create your views here.

# Create recipe View
class RecipeListCreateView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeListSerializer(recipes, many=True)  # Use RecipeListSerializer for listing
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeCreateSerializer(data=request.data)  # Use RecipeCreateSerializer for creation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailView(APIView):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeListSerializer(recipe)  # Use RecipeListSerializer for retrieving a single recipe
        return Response(serializer.data)

    def put(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeUpdateSerializer(recipe, data=request.data)  # Use RecipeUpdateSerializer for updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
