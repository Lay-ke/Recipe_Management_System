from django.urls import path
from .views import CategoryListCreateView, CategoryRecipesView, CategoryDetailView


urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:id>/recipes/', CategoryRecipesView.as_view(), name='category-recipes'),
]