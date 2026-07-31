from django.urls import path
from .views import MealPlanCreateUpdateRemove, MealPlanList, MealPlanDisplay, MealCreateRemove

urlpatterns = [
    path("mealplans-modify/<int:plan_id>", MealPlanCreateUpdateRemove.as_view(), name="mealplans-modify"),
    path("mealplans/", MealPlanList.as_view(), name="mealplans"),
    path("meals/", MealPlanDisplay.as_view(), name="meals-modify"),
    path("meals-modify/<int:meal_id>", MealCreateRemove.as_view(), name="meals"),
]