from django.urls import path
from .views import MatchingFoodsView, RetrieveFoodView

urlpatterns = [
    path("matching-foods/", MatchingFoodsView.as_view(), name="matching-foods"),
    path("retrieve-food/<int:food_id>", RetrieveFoodView.as_view(), name="retrieve-food"),
]