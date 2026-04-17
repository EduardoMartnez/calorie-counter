import csv
from models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients

with open('wweia_food_category.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 0. "wweia_food_category" 1. "wweia_food_category_description" - wweia_food_category.csv
        # 0. food_category_id      1. "description"                     - database
        FoodCategories.objects.create(food_category_id=int(line[0]), description=line[1])

with open('food.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 0. "fdc_id" 2. "data_type" 2. "description" 3. "food_category_id" 4."publication_date" - foods.csv
        # 0. fdc_id                  1. "description" 2. food_category_id                       - database
        Foods.objects.create(fdc_id=int(line[0]), description=line[2], food_category_id=int(line[3]))

with open('food_portion.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 0. "id" 1. "fdc_id" 2. "seq_num" 3. "amount" 4. "measure_unit_id" 5. "portion_description" 6. "modifier" 7. "gram_weight" 8. "data_points" 9. "footnote" 10. "min_year_acquired" - food_portion.csv
        # 0. id   1. fdc_id   2. seq_num                                    3. "description"                       4. gram_weight                                                          - database
        FoodPortions.objects.create(id=int(line[0]), fdc_id=int(line[1]), seq_num=int(line[2]), description=line[3], gram_weight=float(line[4]))

with open('food.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 1. "fdc_id" 2. "data_type" 3. "description" 4."food_category_id" 5."publication_date" - foods.csv
        # 1. fdc_id                  2. "description" 3. food_category_id                       - database
        FoodNutrients.objects.create(fdc_id=int(line[0]), description=line[2], food_category_id=int(line[3]))

with open('food.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 1. "fdc_id" 2. "data_type" 3. "description" 4."food_category_id" 5."publication_date" - foods.csv
        # 1. fdc_id                  2. "description" 3. food_category_id                       - database
        Nutrients.objects.create(fdc_id=int(line[0]), description=line[2], food_category_id=int(line[3]))

with open('food.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 1. "fdc_id" 2. "data_type" 3. "description" 4."food_category_id" 5."publication_date" - foods.csv
        # 1. fdc_id                  2. "description" 3. food_category_id                       - database
        Ingredients.objects.create(fdc_id=int(line[0]), description=line[2], food_category_id=int(line[3]))