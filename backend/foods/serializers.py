from rest_framework import serializers
from .models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients

# Basic Serializers
class FoodNutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrients
        fields = ['id',         # Unique ID of a food's nutrient
                  'food',       # Unique ID of a food
                  'nutrient',   # Unique ID of a nutrient
                  'amount'      # Amount of nutrient in grams
                  ]
        
class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id',             # Unique ID for a food
                  'description',    # Describing what the food is (ex. burger with buns)
                  'food_category',   # Unique ID for a category of food
                  ]

# Advanced Serializers for views.py
class MatchingFoodsSerializer(FoodsSerializer):
    calories = serializers.SerializerMethodField()
    #category = serializers.SerializerMethodField()

    # Uses prefetched foodnutrients_set to find the calories for each food
    def get_calories(self, obj):
        calories = obj.foodnutrients_set.filter(nutrient=208)
        return FoodNutrientsSerializer(calories, many=True).data if calories.exists() else None

    class Meta(FoodsSerializer.Meta):
        model = Foods
        fields = FoodsSerializer.Meta.fields + ['calories']