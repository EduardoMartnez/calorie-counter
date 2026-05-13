from django.contrib import admin
from .models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients

admin.site.register(FoodCategories)
admin.site.register(Foods)
admin.site.register(FoodPortions)
admin.site.register(FoodNutrients)
admin.site.register(Nutrients)
admin.site.register(Ingredients)
