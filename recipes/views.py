from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializers import RecipeCreateSerializer, RecipeUpdateSerializer, RecipeListSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# Create recipe View
class RecipeListCreateView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        paginator = Paginator(recipes, 10)  # 10 recipes per page
        page = request.query_params.get('page', 1)
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = []
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RecipeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailView(APIView):
    def get(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeListSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeUpdateSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        recipes = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(description__icontains=query)
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRecipesView(APIView):
    def get(self, request, id):
        recipes = Recipe.objects.filter(created_by_id=id)
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
