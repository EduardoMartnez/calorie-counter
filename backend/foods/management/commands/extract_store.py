import csv
import logging
from django.core.management.base import BaseCommand
from foods.models import FoodCategories, Foods, FoodPortions, FoodNutrients, Nutrients, Ingredients

class Command(BaseCommand):
    help = "Populates the database with data from Food Data Central"

    def handle(self, *args, **options):
        logger = logging.getLogger("django")

        logger.info("Starting food categories!")
        with open('foods/data/wweia_food_category.csv', mode = 'r') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                # 0. "wweia_food_category" 1. "wweia_food_category_description" - wweia_food_category.csv
                # 0. id                    1. "description"                     - database
                FoodCategories.objects.get_or_create(id=int(row[0]), description=row[1])
        logger.info("Ending food categories!")

        logger.info("Starting foods!")
        with open('foods/data/food.csv', mode = 'r') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                # 0. "fdc_id" 1. "data_type" 2. "description" 3. "food_category_id" 4."publication_date" - foods.csv
                # 0. id                      1. "description" 2. food_category_id                       - database
                Foods.objects.get_or_create(id=int(row[0]), description=row[2], food_category_id_id=int(row[3]))
        logger.info("Ending foods!")

        logger.info("Starting food portions!")
        with open('foods/data/food_portion.csv', mode = 'r') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                # 0. "id" 1. "fdc_id" 2. "seq_num" 3. "amount" 4. "measure_unit_id" 5. "portion_description" 6. "modifier" 7. "gram_weight" 8. "data_points" 9. "footnote" 10. "min_year_acquired" - food_portion.csv
                # 0. id   1. fdc_id   2. seq_num                                    3. "description"                       4. gram_weight                                                          - database
                FoodPortions.objects.get_or_create(id=int(row[0]), fdc_id_id=int(row[1]), seq_num=int(row[2]), description=row[5], gram_weight=float(row[7]))
        logger.info("Ending food portions!")

        logger.info("Starting nutrients!")
        with open('foods/data/nutrient.csv', mode = 'r') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                # 0. "id" 1. "name" 2. "unit_name" 3. "nutrient_nbr" 4. "rank" - nutrient.csv
                #         1. "name" 2. "unit_name" 0. id             3. rank   - database
                Nutrients.objects.get_or_create(id=int(row[3]), name=row[1], unit_name=row[2], rank=float(row[4]))
        logger.info("Ending nutrients!")

        logger.info("Starting food nutrients!")
        with open('foods/data/food_nutrient.csv', mode = 'r') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                # 0. "id" 1. "fdc_id" 2. "nutrient_id" 3. "amount" 4. "data_points" 5. "derivation_id" 6. "min" 7. "max" 8. "median" 9. "footnote" 10. "min_year_acquired" - food_nutrient.csv
                # 0. id   1. fdc_id   2. nutrient_id   3. amount                                                                                                           - database
                FoodNutrients.objects.get_or_create(id=int(row[0]), fdc_id_id=int(row[1]), nutrient_id_id=int(row[2]), amount=float(row[3]))
        logger.info("Ending food nutrients!")
        
        logger.info("Starting ingredients!")
        with open('foods/data/input_food.csv', mode = 'r') as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                # 0. "id" 1. "fdc_id" 2. "fdc_of_input_food" 3. "seq_num" 4. "amount" 5. "sr_code" 6. "sr_description" 7. "unit" 8. "portion_code" 9. "portion_description" 10. "gram_weight" 11. "retention_code" - input_food.csv
                # 0. id   1. fdc_id                          2. seq_num                            3. "description"                                                         4. gram_weight                         - database
                Ingredients.objects.get_or_create(id=int(row[0]), fdc_id_id=int(row[1]), seq_num=int(row[3]), description=row[6], gram_weight=float(row[10]))
        logger.info("Ending ingredients!")