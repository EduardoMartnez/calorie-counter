from django.shortcuts import render
from .models import MealPlans, Meals
from .serializers import MealPlanSerializer, MealPlanFullSerializer, MealSerializer
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

class MealPlanCreateUpdateRemove(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MealPlanSerializer

    # Create a meal plan
    def post(self, request, plan_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update a meal plan (for now, just the name)
    def put(self, request, plan_id):
        mealplan = MealPlans.objects.get(id=plan_id, user=request.user)
        serializer = MealPlanSerializer(mealplan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a meal plan, along with all of the meals associated with it
    def delete(self, request, plan_id):
            mealplan = MealPlans.objects.get(id=plan_id, user=request.user)
            if mealplan:
                mealplan.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MealPlanList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MealPlanSerializer

    # Present a user with all of their meal plans
    def get(self, request):
        mealplan = MealPlans.objects.filter(user=request.user)
        serializer = self.serializer_class(mealplan, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MealPlanDisplay(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MealPlanFullSerializer

    # Display the meals of a meal plan to a user
    def get(self, request):
        id = request.query_params.get('id')
        mealplan = MealPlans.objects.get(id=id, user=request.user)
        mealplan = mealplan.prefetch_related("meal_set")
        serializer = self.serializer_class(mealplan)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MealCreateRemove(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MealSerializer

    # Create a meal for a user's meal plan
    def post(self, request, meal_id):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a meal plan for a user
    def delete(self, request, meal_id):
        meal = Meals.objects.get(id=meal_id)
        if meal:
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)