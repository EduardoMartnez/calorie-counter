from django.shortcuts import render
from django.db.models import Q
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients
from .serializers import MatchingFoodsSerializer

class MatchingFoodsView(APIView):
    serializer_class = MatchingFoodsSerializer # FoodsSerializer

    def get(self, request):
        pattern = request.query_params.get('pattern') # Consider building strings from pattern and how that would work with regex

        # Retrieve all of the foods whose description or category matches the regex pattern
        foods = Foods.objects.filter(Q(description__iregex=pattern) | Q(food_category__description__iregex=pattern))

        # Retrieve the all of the nutrients that belong to each food, for the purpose of picking out the calories for each food
        foods = foods.prefetch_related("foodnutrients_set")

        foods = foods.select_related("food_category")

        serializer = self.serializer_class(foods, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)