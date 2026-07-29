from django.urls import path
from .views import MealPlanCreateUpdateRemove, MealPlanList, MealPlanDisplay, MealCreateRemove

urlpatterns = [
    path("mealplans-modify/", MealPlanCreateUpdateRemove.as_view(), name="mealplans-modify"),
    path("mealplans/", MealPlanList.as_view(), name="mealplans"),
    path("meals/", MealPlanDisplay.as_view(), name="meals-modify"),
    path("meals-modify/", MealCreateRemove.as_view(), name="meals"),
]