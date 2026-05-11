from django.shortcuts import render
from django.db.models import Q, OuterRef, Prefetch
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients
from .serializers import MatchingFoodsSerializer, RetrieveFoodSerializer

class MatchingFoodsView(APIView):
    serializer_class = MatchingFoodsSerializer # FoodsSerializer

    def get(self, request):
        pattern = request.query_params.get('pattern') # Consider building strings from pattern and how that would work with regex

        # Retrieve all of the foods whose description or category matches the regex pattern
        foods = Foods.objects.filter(Q(description__iregex=pattern) | Q(food_category__description__iregex=pattern))

        # Retrieve the all of the nutrients that belong to each food, for the purpose of picking out the calories for each food
        calories = FoodNutrients.objects.filter(nutrient=208)
        foods = foods.prefetch_related(Prefetch("foodnutrients_set", calories))

        # Retrieve the category of each food
        foods = foods.select_related("food_category")

        serializer = self.serializer_class(foods, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RetrieveFoodView(APIView):
    serializer_class = RetrieveFoodSerializer # FoodsSerializer

    def get(self, request, food_id):
        # Start building the QuerySet for retrieving the food and all of it's information
        food = Foods.objects.all()

        nutrients = FoodNutrients.objects.select_related("nutrient")
        # Retrieve all of the nutrients that belong to the food
        food = food.prefetch_related(Prefetch("foodnutrients_set", nutrients))

        # Retrieve all of the portions that exist for the food
        food = food.prefetch_related("foodportions_set")

        # Retrieve all of the ingredients that exist for the food
        food = food.prefetch_related("ingredients_set")

        # Retrieve the category of the food
        food = food.select_related("food_category")

        # Retrieve the specific food that is attached to the provided ID
        food = food.get(id=food_id)

        serializer = self.serializer_class(food)

        return Response(serializer.data, status=status.HTTP_200_OK)