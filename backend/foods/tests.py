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

        #print(foods)

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
    
    def test_retrieve_food(self):
        response_get = client.get("/api/foods/retrieve-food/2705384",
                                    format='json')

        assert response_get.status_code == 200

        food = response_get.data

        #print(food)

        # Food information
        assert food['id'] == 2705384
        assert food['description'] == "Milk, NFS"
        # Food category information
        assert food['food_category']['id'] == 1004
        assert food['food_category']['description'] == "Milk, reduced fat"
        # Food nutrient information
        assert food['nutrients'][0]['food'] == 2705384
        assert food['nutrients'][0]['nutrient']['id'] == 301
        assert food['nutrients'][0]['nutrient']['name'] == "Calcium, Ca"
        assert food['nutrients'][0]['nutrient']['unit_name'] == "MG"
        assert food['nutrients'][0]['nutrient']['rank'] ==  5300.0
        assert food['nutrients'][0]['amount'] == 125.0
        # Food portion information
        assert food['portions'][0]['food'] == 2705384
        assert food['portions'][0]['seq_num'] == 5
        assert food['portions'][0]['description'] == "Guideline amount per cup of hot cereal"
        assert food['portions'][0]['gram_weight'] == 61.0
        # Food ingredient information
        assert food['ingredients'][0]['food'] == 2705384
        assert food['ingredients'][0]['seq_num'] == 1
        assert food['ingredients'][0]['description'] == "Milk, whole, 3.25% milkfat, with added vitamin D"
        assert food['ingredients'][0]['gram_weight'] == 40.0