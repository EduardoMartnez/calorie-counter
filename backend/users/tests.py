import pytest
from rest_framework.test import APIClient
from users.models import CustomUser

pytestmark = pytest.mark.django_db(transaction=False)
client = APIClient()

class TestUsers:
    def test_user_register(self):
        # Create a user in the database
        response_register = client.post("/api/users/register/", {'email': 'eddy@mail.com', 'username': 'Eddy', 'password': '3ddy'}, format='json')
        print("User Registration info: " + str(response_register.data))
        assert response_register.status_code == 201
        response_login = client.post("/api/users/login/", {'email': 'eddy@mail.com', 'password': '3ddy'}, format='json')
        print("User Login info: " + str(response_login.data))
        assert response_login.status_code == 200