from django.test import TestCase

import pytest
from rest_framework.test import APIClient
from .models import Foods, FoodNutrients

pytestmark = pytest.mark.django_db
client = APIClient()

class TestFoods:
    def test_food_matching(self):
        response_get = client.get("/matching-foods?pattern=milk")

        assert response_get.status_code == 200

        foods = response_get.data

        assert foods[0]['description'] == "Milk, Human"