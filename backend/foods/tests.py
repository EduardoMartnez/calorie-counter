from django.test import TestCase

import pytest
from rest_framework.test import APIClient
from .models import Foods, FoodNutrients

pytestmark = pytest.mark.django_db(transaction=False)
client = APIClient()

class TestFoods:
    def test_food_matching(self):
        response_get = client.get("/api/foods/matching-foods",
                                  {"pattern": "milk"}, format='json')

        assert response_get.status_code == 200

        foods = response_get.data[1]

        print(foods)

        # Food information
        assert foods['id'] == 2705384
        assert foods['description'] == "Milk, NFS"
        # Food category information
        assert foods['food_category']['id'] == 1004
        assert foods['food_category']['description'] == "Milk, reduced fat"
        # Food nutrient information
        assert foods['calories'][0]['food'] == 2705384
        assert foods['calories'][0]['nutrient'] == 208 # Nutrient ID for "Energy"
        assert foods['calories'][0]['amount'] == 52.0