from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView
from reviews.views import ReviewListCreateView

urlpatterns = [
    path('', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('<int:recipe_id>/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]