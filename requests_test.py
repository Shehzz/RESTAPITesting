import pytest
import requests
import variables


def test_checking_for_200_status(URL):
    response = requests.get(URL).json()
    assert response['code'] == 200


def test_checking_for_deleted_user(URL):
    get_response_body = requests.get(URL + "12341111").json()
    assert get_response_body['code'] == 404
    print("\nThe HTTP response code received is:" + str(get_response_body['code']))


# Verifying the body of the response headers
def test_check_content_type_equals_json(URL):
    response = requests.get(URL)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_creating_a_new_user_using_POST_123(URL, auth_token):
    response = requests.post(URL, headers=auth_token, data=variables.payload)
    response_json = response.json()

    #global response_id  # TODO Change this to a fixture for later use

    response_id = response_json['data']['id']
    pytest.global_response_id = response_id
    print("\nThe userID generated is:" + str(response_id))
    assert response_json['code'] == 201


def test_checking_for_same_existing_user_123(URL):
    # TODO MAKE A GENERIC FUNCTION(FIXTURE) TO DO ALL THE GET ACTIONS
    response = requests.get(URL + str(pytest.global_response_id)).json()
    assert response['code'] == 200
    print("\nThe HTTP response code received is:" + str(response['code']))
