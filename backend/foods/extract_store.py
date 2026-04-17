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
        FoodPortions.objects.create(id=int(line[0]), fdc_id=int(line[1]), seq_num=int(line[2]), description=line[5], gram_weight=float(line[7]))

with open('nutrient.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 0. "id" 1. "name" 2. "unit_name" 3. "nutrient_nbr" 4. "rank" - nutrient.csv
        #         1. "name" 2. "unit_name" 0. nutrient_id    3. rank   - database
        Nutrients.objects.create(nutrient_id=int(line[3]), name=line[1], unit_name=line[2], rank=float(line[4]))

with open('food_nutrient.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 0. "id" 1. "fdc_id" 2. "nutrient_id" 3. "amount" 4. "data_points" 5. "derivation_id" 6. "min" 7. "max" 8. "median" 9. "footnote" 10. "min_year_acquired" - food_nutrient.csv
        # 0. id   1. fdc_id   2. nutrient_id   3. amount                                                                                                           - database
        FoodNutrients.objects.create(id=int(line[0]), fdc_id=int(line[1]), nutrient_id=int(line[2]), amount=float(line[3]))

with open('input_food.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for i in range(1, len(csv_file)):
        line = csv_file[i]
        # 0. "id" 1. "fdc_id" 2. "fdc_of_input_food" 3. "seq_num","amount" 4. "sr_code" 5. "sr_description" 6. "unit" 7. "portion_code" 8. "portion_description" 9. "gram_weight" 10. "retention_code" - input_food.csv
        # 0. id   1. fdc_id                          2. seq_num                         3. "description"                                                         4. gram_weight                        - database
        Ingredients.objects.create(id=int(line[0]), fdc_id=int(line[1]), seq_num=int(line[3]), description=line[5], gram_weight=float(line[9]))