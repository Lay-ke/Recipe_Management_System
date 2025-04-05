from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializers import RecipeSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# View for listing and creating recipes
class RecipeListCreateView(APIView):
    def get(self, request):
        # Fetch all recipes and paginate them (10 per page)
        recipes = Recipe.objects.all()
        paginator = Paginator(recipes, 10)
        page = request.query_params.get('page', 1)
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = []
        # Serialize and return paginated recipes
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new recipe
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for retrieving, updating, and deleting a specific recipe
class RecipeDetailView(APIView):
    def get(self, request, id):
        # Fetch a recipe by ID
        recipe = get_object_or_404(Recipe, recipe_id=id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        # Update a recipe by ID
        recipe = get_object_or_404(Recipe, recipe_id=id)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        # Delete a recipe by ID
        recipe = get_object_or_404(Recipe, recipe_id=id)
        recipe.delete()
        return Response({"message": "Delete successful."}, status=status.HTTP_204_NO_CONTENT)

# View for searching recipes by title or description
class RecipeSearchView(APIView):
    def get(self, request):
        # Search recipes using query parameter 'q'
        query = request.query_params.get('q', '')
        recipes = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(description__icontains=query)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View for fetching recipes created by a specific user
class UserRecipesView(APIView):
    def get(self, request, id):
        # Fetch recipes created by a user with the given ID
        recipes = Recipe.objects.filter(created_by_id=id)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
