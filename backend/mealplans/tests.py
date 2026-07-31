import pytest
from rest_framework.test import APIClient
from users.models import CustomUser

pytestmark = pytest.mark.django_db(transaction=False)
client = APIClient()

class TestMealPlans:
    def test_mealplan_create(self):
        # Authenticate the user for the test
        user = CustomUser.objects.create_user(email='eddy@mail.com', username='Eddy', password='3ddy')
        client.force_authenticate(user=user)
        print("User authenticated")

        # Create a meal plan
        response_meal = client.post("/api/mealplans/mealplans-modify/0", {'description': 'Protein Max'}, format='json')
        print("Meal Creation info: " + str(response_meal.data))
        assert response_meal.data["id"] == 1
        assert response_meal.data["user"] == 1
        assert response_meal.data["description"] == "Protein Max"
        assert response_meal.status_code == 201

    def test_mealplan_update(self):
        # Authenticate the user for the test
        user = CustomUser.objects.create_user(email='eddy@mail.com', username='Eddy', password='3ddy',)
        client.force_authenticate(user=user)
        print("User authenticated")

        # Create a meal plan
        response_meal = client.post("/api/mealplans/mealplans-modify/0", {'description': 'Protein Max'}, format='json')
        #print("Meal Creation info: " + str(response_meal.data))
        #assert response_meal.data["id"] == 1
        #assert response_meal.data["user"] == 1
        #assert response_meal.data["description"] == "Protein Max"
        #assert response_meal.status_code == 201

        # Update the description of a meal plan
        response_meal = client.put("/api/mealplans/mealplans-modify/1", {'description': 'Protein Max (Vegan)'}, format='json')
        assert response_meal.data["description"] == "Protein Max (Vegan)"
        assert response_meal.status_code == 200

    def test_mealplan_delete(self):
        # Authenticate the user for the test
        user = CustomUser.objects.create_user(email="eddy@mail.com", username="Eddy", password="3ddy",)
        client.force_authenticate(user=user)
        print("User authenticated")

        # Create a meal plan
        response_meal = client.post("/api/mealplans/mealplans-modify/0", {'description': 'Protein Max'}, format='json')
        #print("Meal Creation info: " + str(response_meal.data))
        #assert response_meal.data["id"] == 1
        #assert response_meal.data["user"] == 1
        #assert response_meal.data["description"] == "Protein Max"
        #assert response_meal.status_code == 201

        # Update the description of a meal plan
        response_meal = client.delete("/api/mealplans/mealplans-modify/1", format='json')
        assert response_meal.status_code == 204