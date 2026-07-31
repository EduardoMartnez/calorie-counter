from rest_framework import serializers
from .models import MealPlans, Meals

# Basic Serializers
class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlans
        fields = ['id',             # Unique ID for a meal plan
                  'user',           # User that owns the meal plan
                  'description',    # Describing what the meal plan is, determined by the user
                  ]
        read_only_fields = ["user"]

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ['id',         # Unique ID for a food
                  'mealplan',   # The meal plan that uses this meal
                  'food',       # The food being used for the meal
                  'motd',       # Determines what meal of the day it is
                  ]
        
# Advanced Serializers for views.py
class MealPlanFullSerializer(MealPlanSerializer):
    meals = serializers.SerializerMethodField()

    # Uses prefetched meal_set to find the meals for a meal plan
    def get_meals(self, obj):
        meals = obj.meal_set.all()
        return MealSerializer(meals, many=True).data if meals else None

    class Meta(MealPlanSerializer.Meta):
        model = MealPlans
        fields = MealPlanSerializer.Meta.fields + ['meals']