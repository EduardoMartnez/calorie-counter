from rest_framework import serializers
from .models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients

# Basic Serializers
class FoodCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategories
        fields = ['id',             # Unique ID for a category
                  'description',    # Describing what the category is
                  ]

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id',             # Unique ID for a food
                  'description',    # Describing what the food is (ex. burger with buns)
                  'food_category',   # Unique ID for a category of food
                  ]

class FoodNutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrients
        fields = ['id',         # Unique ID of a food's nutrient
                  'food',       # Unique ID of a food
                  'nutrient',   # Unique ID of a nutrient
                  'amount'      # Amount of nutrient in grams
                  ]

# Advanced Serializers for views.py
class MatchingFoodsSerializer(FoodsSerializer):
    calories = serializers.SerializerMethodField()
    food_category = serializers.SerializerMethodField()

    # Uses prefetched foodnutrients_set to find the calories for each food
    def get_calories(self, obj):
        calories = obj.foodnutrients_set.all()
        return FoodNutrientsSerializer(calories, many=True).data if calories else None
    
    # Uses searched food to find the category for each food (KCAL)
    def get_food_category(self, obj):
        food_category = obj.food_category
        return FoodCategoriesSerializer(food_category).data if food_category else None

    class Meta(FoodsSerializer.Meta):
        model = Foods
        fields = FoodsSerializer.Meta.fields + ['food_category','calories']