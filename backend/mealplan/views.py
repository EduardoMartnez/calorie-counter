from django.shortcuts import render
from .models import MealPlan
from .serializers import MealPlanSerializer, MealPlanFullSerializer
from rest_framework import mixins, generics, status
from rest_framework.views import APIView, Response

class MealPlanCreate(APIView):
    serializer_class = MealPlanSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if self.request.user and serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealPlanList(APIView):
    serializer_class = MealPlanSerializer

    def get(self, request):
        if self.request.user:
            user_id = self.request.user.id
            id = request.query_params.get('id')
            mealplan = MealPlan.objects.filter(id=id, user__id=user_id)
            serializer = self.serializer_class(mealplan)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
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
    serializer_class = MealPlanFullSerializer

    def get(self, request):
        if self.request.user:
            user_id = self.request.user.id
            id = request.query_params.get('id')
            mealplan = MealPlan.objects.filter(id=id, user__id=user_id)
            mealplan = mealplan.prefetch_related("meal_set")
            serializer = self.serializer_class(mealplan)
            return Response(serializer.data, status=status.HTTP_200_OK)