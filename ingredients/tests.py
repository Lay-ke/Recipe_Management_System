from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class IngredientViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ingredient_list_create_url = reverse('ingredient-list-create')
        self.ingredient_detail_url = lambda id: reverse('ingredient-detail', kwargs={'id': id})
        self.ingredient_recipes_url = lambda id: reverse('ingredient-recipes', kwargs={'id': id})

        # Create a sample ingredient for testing
        self.sample_ingredient = {'name': 'Carrot'}
        response = self.client.post(self.ingredient_list_create_url, self.sample_ingredient, format='json')
        self.ingredient_id = response.data['Ingredient']['ingredient_id']

    def test_list_ingredients(self):
        """Test retrieving a list of ingredients"""
        response = self.client.get(self.ingredient_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_create_ingredient(self):
        """Test creating a new ingredient"""
        payload = {'name': 'Tomato'}
        response = self.client.post(self.ingredient_list_create_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['Ingredient']['name'], payload['name'])

    def test_invalid_create_ingredient(self):
        """Test creating an ingredient with invalid payload"""
        payload = {'name': ''}
        response = self.client.post(self.ingredient_list_create_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_ingredient_detail(self):
        """Test retrieving a single ingredient by ID"""
        response = self.client.get(self.ingredient_detail_url(self.ingredient_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.sample_ingredient['name'])

    def test_update_ingredient(self):
        """Test updating an ingredient"""
        payload = {'name': 'Updated Carrot'}
        response = self.client.put(self.ingredient_detail_url(self.ingredient_id), payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Ingredient']['name'], payload['name'])  # Fixed assertion

    def test_delete_ingredient(self):
        """Test deleting an ingredient"""
        response = self.client.delete(self.ingredient_detail_url(self.ingredient_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Delete successful.')

    def test_get_ingredient_recipes(self):
        """Test retrieving recipes for an ingredient"""
        response = self.client.get(self.ingredient_recipes_url(self.ingredient_id))
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])
        if response.status_code == status.HTTP_200_OK:
            self.assertIsInstance(response.data, list)
        else:
            self.assertEqual(response.data['detail'], 'No recipes found for this ingredient.')
