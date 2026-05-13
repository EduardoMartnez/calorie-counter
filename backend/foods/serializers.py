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
        
class FoodPortionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPortions
        fields = ['id',             # Unique ID of a food's portion
                  'food',           # Unique ID of a food
                  'seq_num',        # Order in which portions are ordered
                  'description',    # Describing what the portion is
                  'gram_weight'     # Weight of a portion in grams
                  ]
        
class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id',             # Unique ID of a food's ingredient
                  'food',           # Unique ID of a food
                  'seq_num',        # Order in which ingredients are ordered
                  'description',    # Describing what the ingredient is
                  'gram_weight'     # Weight of an ingredient in grams
                  ]

class FoodNutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrients
        fields = ['id',         # Unique ID of a food's nutrient
                  'food',       # Unique ID of a food
                  'nutrient',   # Unique ID of a nutrient
                  'amount'      # Amount of nutrient in grams
                  ]
        
class NutrientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrients
        fields = ['id',         # Unique ID of a nutrient
                  'name',       # Name of a nutrient
                  'unit_name',  # Measurement unit for the nutrient
                  'rank'        # Order in which the nutrient is displayed
                  ]
        
class FoodNutrientInformationSerializer(FoodNutrientsSerializer):
    # Collect information about a nutrient that a food has
    nutrient = serializers.SerializerMethodField()

    def get_nutrient(self, obj):
        nutrient = obj.nutrient
        return NutrientsSerializer(nutrient).data if nutrient else None

    class Meta(FoodNutrientsSerializer.Meta):
        model = FoodNutrients
        fields = FoodNutrientsSerializer.Meta.fields

# Advanced Serializers for views.py
class MatchingFoodsSerializer(FoodsSerializer):
    calories = serializers.SerializerMethodField()
    food_category = serializers.SerializerMethodField()

    # Uses prefetched foodnutrients_set to find the calories for each food
    def get_calories(self, obj):
        calories = obj.foodnutrients_set.all()
        return FoodNutrientsSerializer(calories, many=True).data if calories else None
    
    # Uses related food_category to find the category of each food
    def get_food_category(self, obj):
        food_category = obj.food_category
        return FoodCategoriesSerializer(food_category).data if food_category else None

    class Meta(FoodsSerializer.Meta):
        model = Foods
        fields = FoodsSerializer.Meta.fields + ['calories']

class RetrieveFoodSerializer(FoodsSerializer):
    nutrients = serializers.SerializerMethodField()
    portions = serializers.SerializerMethodField()
    ingredients = serializers.SerializerMethodField()
    food_category = serializers.SerializerMethodField()

    # Uses prefetched foodnutrients_set to find all the nutrients of a food
    def get_nutrients(self, obj):
        nutrients = obj.foodnutrients_set.all()
        return FoodNutrientInformationSerializer(nutrients, many=True).data if nutrients else None
    
    # Uses prefetched foodportions_set to find all the portions of a food
    def get_portions(self, obj):
        portions = obj.foodportions_set.all()
        return FoodPortionsSerializer(portions, many=True).data if portions else None
    
    # Uses prefetched foodportions_set to find all the ingredients of a food
    def get_ingredients(self, obj):
        ingredients = obj.ingredients_set.all()
        return IngredientsSerializer(ingredients, many=True).data if ingredients else None
    
    # Uses related food_category to find the category of each food
    def get_food_category(self, obj):
        food_category = obj.food_category
        return FoodCategoriesSerializer(food_category).data if food_category else None

    class Meta(FoodsSerializer.Meta):
        model = Foods
        fields = FoodsSerializer.Meta.fields + ['nutrients', 'portions', 'ingredients']