from rest_framework import serializers

class FoodsSerializer(serializers.Serializer):
    # Unique ID for a food
    id = serializers.IntegerField()
    # Describing what the food is (ex. burger with buns)
    description = serializers.CharField()
    # Unique ID for a category of food
    food_category_id = serializers.PrimaryKeyRelatedField()