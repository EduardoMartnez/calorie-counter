from django.urls import path
from .views import MatchingFoodsView

urlpatterns = [
    path("matching-foods/", MatchingFoodsView.as_view(), name="matching-foods"),
]