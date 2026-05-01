from django.db import models

class FoodCategories(models.Model):
    # Unique ID for a category of food
    id = models.BigIntegerField(primary_key=True) # wweia_food_category
    # Description of a category of food
    description = models.CharField() # wweia_food_category_description

    def __str__(self):
        return self.description

class Foods(models.Model):
    # Unique ID for a food
    id = models.BigIntegerField(primary_key=True)
    # Describing what the food is (ex. burger with buns)
    description = models.CharField()
    # Unique ID for a category of food
    food_category = models.ForeignKey(FoodCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class FoodPortions(models.Model):
    # Unique ID of a portion
    id = models.BigIntegerField(primary_key=True)
    # Unique ID for a food
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)
    # Order in which portions are ordered
    seq_num = models.SmallIntegerField()
    # Description of a portion
    description = models.CharField() # portion_description
    # Weight of a portion in grams
    gram_weight = models.FloatField() 

    def __str__(self):
        return self.description

class Nutrients(models.Model):
    # Unique ID of a nutrient
    id = models.BigIntegerField(primary_key=True) # nutrient_nbr
    # Name of a nutrient
    name = models.CharField()
    # "GM" for grams, "MG" for milligrams, etc.
    unit_name = models.CharField()
    # Order in which nutrients are displayed
    rank = models.FloatField()

    def __str__(self):
        return self.name

class FoodNutrients(models.Model):
    # Unique ID of a food's nutrient
    id = models.BigIntegerField(primary_key=True)
    # Unique ID of a food
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)
    # Unique ID of a nutrient
    nutrient = models.ForeignKey(Nutrients, on_delete=models.CASCADE)
    # Amount of nutrient in grams
    amount = models.FloatField()

    def __str__(self):
        return self.food.description + ", " + self.nutrient.name

class Ingredients(models.Model):
    # Unique ID for a food's ingredients
    id = models.BigIntegerField(primary_key=True)
    # Unique ID of a food
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)
    # Order in which ingredients are displayed
    seq_num = models.SmallIntegerField()
    # Description of the ingredient
    description = models.CharField() # sr_description
    # Amount of ingredient in grams
    gram_weight = models.FloatField() 

    def __str__(self):
        return self.description