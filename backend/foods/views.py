from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients
from django.db.models import Q

class MatchingFoodAPI(APIView):
    def get(self, request, pattern):
        # Retrieve all of the foods whose description or category matches the regex pattern
        foods = Foods.objects.filter(Q(description__regex=pattern) | Q(food_categories_id__description__iregex=pattern))

        # Retrieve the calories that belong to each food
        food_cals = foods.select_related("food_nutrients__amount")