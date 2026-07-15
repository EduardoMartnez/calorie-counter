from rest_framework import serializers
from .models import MealPlan, Meal

# Basic Serializers
class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ['id',             # Unique ID for a meal plan
                  'user',           # User that owns the meal plan
                  'description',    # Describing what the meal plan is, determined by the user
                  ]

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id',         # Unique ID for a food
                  'mealplan',   # The meal plan that uses this meal
                  'food',       # The food being used for the meal
                  'motd',       # Determines what meal of the day it is
                  ]
        
# Advanced Serializers for views.py
