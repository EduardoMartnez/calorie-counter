import csv
from models import Foods, FoodCategories, FoodPortions, FoodNutrients, Nutrients, Ingredients

with open('food.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 1. "fdc_id" 2. "data_type" 3. "description" 4."food_category_id" 5."publication_date"
        Foods.objects.create(int(line[0]), )