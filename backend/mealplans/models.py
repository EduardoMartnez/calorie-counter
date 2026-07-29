from django.db import models

class MealPlans(models.Model):
    # User that created this meal plan
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    # Name of meal plan
    description = models.CharField()

    def __str__(self):
        return self.description

class Meals(models.Model):
    # Meal plan this meal belongs to
    mealplan = models.ForeignKey(MealPlans, on_delete=models.CASCADE)
    # Food that is being used for this meal
    food = models.ForeignKey("foods.Foods", on_delete=models.CASCADE)
    # Is this meal part of a breakfast, lunch, or dinner?
    motd = models.CharField() # Meal of the Day

    def __str__(self):
        return self.mealplan.description + ", " + self.food.description + ", " + self.motd