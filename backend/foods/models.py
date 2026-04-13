from django.db import models

# Create your models here.
class FoodCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    category_description = models.CharField()

class Foods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    food_description = models.CharField()
    food_category_id = models.ForeignKey(FoodCategories)

class FoodNutrients(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField()

class FoodNutrients(models.Model):
    id = models.BigIntegerField(primary_key=True)
    food_id = models.ForeignKey(Foods)
    nutrient_id = models.ForeignKey(FoodNutrients)
    amount = models.IntegerField()

class FoodPortion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    food_id = models.ForeignKey(Foods)
    seq_num = models.SmallIntegerField()
    portion_description = models.CharField()
    gram_weight = models.IntegerField()