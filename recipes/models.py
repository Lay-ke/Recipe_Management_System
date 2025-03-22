from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField('ingredients.Ingredient', through='recipes.RecipeIngredient')
    instructions = models.TextField()
    prep_time = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=100)
    servings = models.CharField(max_length=100)
    phote = models.ImageField(upload_to='images/')
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    user_id = models.ForeignKey('accounts.CustomUser', related_name='recipes', on_delete=models.CASCADE)
    category_id = models.ForeignKey('categories.Category', related_name='recipes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class RecipeIngredient(models.Model):
    recipe_id = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    unit = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.quantity