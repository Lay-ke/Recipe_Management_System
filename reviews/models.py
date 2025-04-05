from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    user_id = models.ForeignKey('accounts.CustomUser', related_name='reviews', on_delete=models.CASCADE)
    recipe_id = models.ForeignKey('recipes.Recipe', related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user_id', 'recipe_id')

    def __str__(self):
        return f"Review for {self.recipe_id.name} by {self.user_id.username}"