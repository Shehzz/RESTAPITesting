import pytest
import requests
import variables


def test_checking_for_200_status(URL):
    response = requests.get(URL).json()
    assert response['code'] == 200


def test_checking_for_nonexistent_user(URL):
    get_response_body = requests.get(URL + variables.nonexistent_user).json()
    assert get_response_body['code'] == 404 and \
           get_response_body['data']['message'] == "Resource not found"
    print("\nThe user with the ID:" + variables.nonexistent_user + \
          " doesn't exist & the HTTP response code received is:" + str(get_response_body['code']))


def test_creating_a_new_user_using_POST_123(URL, auth_token):
    response = requests.post(URL, headers=auth_token, data=variables.payload)
    response_json = response.json()
    response_id = response_json['data']['id']
    pytest.global_response_id = response_id  # making the response_id a GLOBAL variable
    print("\nThe userID generated is:" + str(response_id))
    assert response_json['code'] == 201
    assert data_verification(URL)  # making sure all the data is verified


def data_verification(URL):
    response = requests.get(URL + str(pytest.global_response_id)).json()
    if response['data']['id'] == pytest.global_response_id and \
            response['data']['name'] == variables.fake_name and \
            response['data']['email'] == variables.fake_email and \
            response['data']['gender'] == "Male" and \
            response['data']['status'] == "Active":
        print("\nData Verification success!")
        print(response)
        return True
    else:
        print("\nData Verification failed!")
        return False


def test_fetching_existing_user_using_GET(URL):
    response = requests.get(URL + str(pytest.global_response_id)).json()
    assert response['code'] == 200
    print("\nThe HTTP response code is " + str(response['code']))


def test_updating_existing_user_using_PUT(URL, auth_token):
    response = requests.put(URL + str(pytest.global_response_id), headers=auth_token, data=variables.updated_payload)
    response_json = response.json()
    assert response_json['code'] == 200

    """ If the data_verification() fails here, that means the user ID has been updated successfully"""

    if not (data_verification(URL)):
        print("The user details have been updated successfully!")
        print(response_json)
        assert True
    else:
        print("The user details have not been updated!")
        assert False


def test_deleting_existing_user_using_DELETE_123(URL, auth_token):
    response = requests.delete(URL + str(pytest.global_response_id), headers=auth_token).json()
    assert response['code'] == 204 and \
           response['data'] is None

    """Once the DELETE request is executed, we can verify this by doing a GET request and \
    checking the 404 response code"""

    get_response = requests.get(URL + str(pytest.global_response_id)).json()
    assert get_response['code'] == 404 and \
           get_response['data']['message'] == "Resource not found"
    print("\nThe HTTP response code received is " + str(get_response['code']) + "!" +
          "\nThe user has been deleted successfully!")
