import pytest
from rest_framework.test import APIClient
from users.models import CustomUser
from .models import MealPlans, Meals
from foods.models import Foods

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
        assert response_meal.status_code == 201
        assert response_meal.data["id"] == 1
        assert response_meal.data["user"] == 1
        assert response_meal.data["description"] == "Protein Max"

    def test_mealplan_update(self):
        # Authenticate the user for the test
        user = CustomUser.objects.create_user(email='eddy@mail.com', username='Eddy', password='3ddy',)
        client.force_authenticate(user=user)
        print("User authenticated")

        # Create a meal plan
        mealplan = MealPlans.objects.create(description='Protein Max', user=user)

        # Update the description of a meal plan
        response_meal = client.put("/api/mealplans/mealplans-modify/1", {'description': 'Protein Max (Vegan)'}, format='json')
        assert response_meal.status_code == 200
        assert response_meal.data["description"] == "Protein Max (Vegan)"

    def test_mealplan_delete(self):
        # Authenticate the user for the test
        user = CustomUser.objects.create_user(email="eddy@mail.com", username="Eddy", password="3ddy",)
        client.force_authenticate(user=user)
        print("User authenticated")

        # Create a meal plan
        mealplan = MealPlans.objects.create(description='Protein Max', user=user)

        # Update the description of a meal plan
        response_meal = client.delete("/api/mealplans/mealplans-modify/1", format='json')
        assert response_meal.status_code == 204

    def test_mealplan_list(self):
        # Authenticate the user 1 for the test
        user1 = CustomUser.objects.create_user(email="eddy@mail.com", username="Eddy", password="3ddy",)
        client.force_authenticate(user=user1)
        print("User 1 authenticated")

        # Check for meal plans if no meal plans exist yet
        response_meal = client.get("/api/mealplans/mealplans/", format='json')
        assert response_meal.status_code == 200
        assert response_meal.data == []

        # Create a meal plan for user 1
        mealplan1 = MealPlans.objects.create(description='Protein Max', user=user1)
        mealplan2 = MealPlans.objects.create(description='Protein Max (Vegan)', user=user1)
        mealplan3 = MealPlans.objects.create(description='Fiber Max', user=user1)
        mealplan4 = MealPlans.objects.create(description='Pure Fruits', user=user1)
        mealplan5 = MealPlans.objects.create(description='Pure Veggies', user=user1)

        # Retrieve a list of meal plans by user 1
        response_meal1 = client.get("/api/mealplans/mealplans/", format='json')
        assert response_meal1.status_code == 200
        assert len(response_meal1.data) == 5
        assert response_meal1.data[0]["id"] == 1
        assert response_meal1.data[0]["user"] == 1
        assert response_meal1.data[0]["description"] == "Protein Max"
        assert response_meal1.data[1]["id"] == 2
        assert response_meal1.data[1]["user"] == 1
        assert response_meal1.data[1]["description"] == "Protein Max (Vegan)"
        assert response_meal1.data[2]["id"] == 3
        assert response_meal1.data[2]["user"] == 1
        assert response_meal1.data[2]["description"] == "Fiber Max"
        assert response_meal1.data[3]["id"] == 4
        assert response_meal1.data[3]["user"] == 1
        assert response_meal1.data[3]["description"] == "Pure Fruits"
        assert response_meal1.data[4]["id"] == 5
        assert response_meal1.data[4]["user"] == 1
        assert response_meal1.data[4]["description"] == "Pure Veggies"

        # Authenticate the user 2 for the test
        client.force_authenticate(user=None)
        user2 = CustomUser.objects.create_user(email="martin@mail.com", username="Martin", password="mart1n",)
        client.force_authenticate(user=user2)
        print("User 2 authenticated")

        # Create a meal plan for user 2
        mealplan6 = MealPlans.objects.create(description='Sweets Max', user=user2)

        # Retrieve a list of meal plans by user 1
        response_meal2 = client.get("/api/mealplans/mealplans/", format='json')
        assert response_meal2.status_code == 200
        assert len(response_meal2.data) == 1
        assert response_meal2.data[0]["id"] == 6
        assert response_meal2.data[0]["user"] == 2
        assert response_meal2.data[0]["description"] == "Sweets Max"

    def test_mealplan_detail(self):
        # Authenticate the user 1 for the test
        user1 = CustomUser.objects.create_user(email="eddy@mail.com", username="Eddy", password="3ddy",)
        client.force_authenticate(user=user1)
        print("User 1 authenticated")

        # Check for meal plans if no meal plans exist yet
        response_meal = client.get("/api/mealplans/mealplans/", format='json')
        assert response_meal.status_code == 200
        assert response_meal.data == []

        # Create a meal plan for user 1
        mealplan1 = MealPlans.objects.create(description='Protein Max', user=user1)
        mealplan2 = MealPlans.objects.create(description='Protein Max (Vegan)', user=user1)
        mealplan3 = MealPlans.objects.create(description='Fiber Max', user=user1)
        mealplan4 = MealPlans.objects.create(description='Pure Fruits', user=user1)
        mealplan5 = MealPlans.objects.create(description='Pure Veggies', user=user1)

        # Retrieve a list of meal plans by user 1
        response_meal1 = client.get("/api/mealplans/mealplans/", format='json')
        assert response_meal1.status_code == 200
        assert len(response_meal1.data) == 5
        assert response_meal1.data[0]["id"] == 1
        assert response_meal1.data[0]["user"] == 1
        assert response_meal1.data[0]["description"] == "Protein Max"
        assert response_meal1.data[1]["id"] == 2
        assert response_meal1.data[1]["user"] == 1
        assert response_meal1.data[1]["description"] == "Protein Max (Vegan)"
        assert response_meal1.data[2]["id"] == 3
        assert response_meal1.data[2]["user"] == 1
        assert response_meal1.data[2]["description"] == "Fiber Max"
        assert response_meal1.data[3]["id"] == 4
        assert response_meal1.data[3]["user"] == 1
        assert response_meal1.data[3]["description"] == "Pure Fruits"
        assert response_meal1.data[4]["id"] == 5
        assert response_meal1.data[4]["user"] == 1
        assert response_meal1.data[4]["description"] == "Pure Veggies"

    def test_mealplan_display(self):
        # Authenticate the user 1 for the test
        user1 = CustomUser.objects.create_user(email="eddy@mail.com", username="Eddy", password="3ddy",)
        client.force_authenticate(user=user1)
        print("User 1 authenticated")

        # Check for meal plans if no meal plans exist yet
        response_meal = client.get("/api/mealplans/mealplans/", format='json')
        assert response_meal.status_code == 200
        assert response_meal.data == []

        # Create a meal plan for user 1
        mealplan1 = MealPlans.objects.create(description='Protein Max', user=user1)
        food1 = Foods.objects.get(id=2707515)
        
        # Add a meal to the mealplan
        client.post("/api/mealplans/meals-modify/0", {'mealplan': 1, 'food': 2707515, 'motd': 'Breakfast'}, format='json')

        # Check meal plan
        response_mealplan1 = client.get("/api/mealplans/meals/?id=1", format='json')
        assert response_mealplan1.status_code == 200
        assert response_mealplan1.data["id"] == 1
        assert response_mealplan1.data["user"] == 1
        assert response_mealplan1.data["description"] == "Protein Max"
        assert response_mealplan1.data['meals'][0]["mealplan"] == 1
        assert response_mealplan1.data['meals'][0]["food"] == 2707515
        assert response_mealplan1.data['meals'][0]["motd"] == "Breakfast"

        # Remove a meal from the mealplan
        client.delete("/api/mealplans/meals-modify/1", format='json')

        # Check meal plan again
        response_mealplan2 = client.get("/api/mealplans/meals/?id=1", format='json')
        assert response_mealplan2.status_code == 200
        assert response_mealplan2.data['meals'] == None