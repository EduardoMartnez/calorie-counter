from django.shortcuts import render
from .models import MealPlan
from .serializers import MealPlanSerializer, MealPlanFullSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView


class MealPlanList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class MealPlanDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class MealPlanDisplay(APIView):
    serializer_class = MealPlanFullSerializer # FoodsSerializer

    def get(self, request):
        if self.request.user:
            user = self.request.user
            id = request.query_params.get('id')
            mealplan = MealPlan.objects.filter(id=id, user=user)