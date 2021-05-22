import pytest
import variables


@pytest.fixture
def URL():
    API_URL = "https://gorest.co.in/public-api/users/"
    return API_URL


@pytest.fixture
def auth_token():
    auth_header = {'Authorization': 'Bearer ' + variables.AUTH}
    return auth_header
