from django.urls import path
from .views import IngredientListCreateView, IngredientDetailUpdateDeleteView, IngredientRecipesView

urlpatterns = [
    path('', IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('<int:id>/', IngredientDetailUpdateDeleteView.as_view(), name='ingredient-detail'),
    path('<int:id>/recipes/', IngredientRecipesView.as_view(), name='ingredient-recipes'),
]