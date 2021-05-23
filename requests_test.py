import pytest
import requests
import variables


@pytest.mark.positive
def test_checking_for_active_endpoint(URL):
    response = requests.get(URL).json()
    assert response['code'] == 200


@pytest.mark.positive
def test_creating_a_new_user_using_POST(URL, auth_token):
    response = requests.post(URL, headers=auth_token, data=variables.payload)
    response_json = response.json()
    response_id = response_json['data']['id']
    pytest.global_response_id = response_id  # making the response_id a GLOBAL variable
    print("\nThe userID generated is:" + str(response_id))
    assert response_json['code'] == 201
    assert variables.data_verification(URL)  # making sure all the data is verified


@pytest.mark.positive
def test_fetching_existing_user_using_GET(URL):
    response = requests.get(URL + str(pytest.global_response_id)).json()
    assert response['code'] == 200
    print("\nThe HTTP response code is " + str(response['code']))


@pytest.mark.positive
def test_updating_existing_user_using_PUT(URL, auth_token):
    response = requests.put(URL + str(pytest.global_response_id), headers=auth_token, data=variables.updated_payload)
    response_json = response.json()
    assert response_json['code'] == 200

    """ If the data_verification() fails here, that means the user ID has been updated 
        successfully"""

    if not (variables.data_verification(URL)):
        print("The user details have been updated successfully!")
        print(response_json)
        assert True
    else:
        print("The user details have not been updated!")
        assert False


@pytest.mark.positive
def test_deleting_existing_user_using_DELETE(URL, auth_token):
    response = requests.delete(URL + str(pytest.global_response_id), headers=auth_token).json()
    assert response['code'] == 204 and \
           response['data'] is None

    """Once the DELETE request is executed, we can verify this by doing a GET request and 
       checking the 404 response code"""

    get_response = requests.get(URL + str(pytest.global_response_id)).json()
    assert get_response['code'] == 404 and \
           get_response['data']['message'] == "Resource not found"
    print("\nThe HTTP response code received is " + str(get_response['code']) + "!" +
          "\nThe user has been deleted successfully!")


@pytest.mark.negative
def test_faulty_payload_using_POST(URL, auth_token):
    response = requests.post(URL, headers=auth_token, data=variables.faulty_payload).json()
    assert response['code'] == 422 and \
           response['data'][0]['field'] == "email"
    print("\nThe HTTP response code received is " + str(response['code']) +
          "! Email cannot be blank!")


@pytest.mark.negative
def test_deleting_nonexistent_user(URL, auth_token):
    response = requests.delete(URL + variables.nonexistent_user, headers=auth_token).json()
    assert response['code'] == 404
    print("\nThe HTTP response code received is " + str(response['code']) +
          "! Cannot delete a user that doesn't exist!")


@pytest.mark.negative
def test_faulty_auth_key(URL, faulty_auth_token):
    response = requests.post(URL, headers=faulty_auth_token, data=variables.payload)
    response_json = response.json()
    assert response_json['code'] == 401 and \
           response_json['data']['message'] == "Authentication failed"
    print("\n" + str(response_json['data']['message']) +
          "! Please check the AUTH key!")


@pytest.mark.negative
def test_checking_for_nonexistent_user(URL):
    get_response_body = requests.get(URL + variables.nonexistent_user).json()
    assert get_response_body['code'] == 404 and \
           get_response_body['data']['message'] == "Resource not found"
    print("\nThe user with the ID:" + variables.nonexistent_user +
          " doesn't exist & the HTTP response code received is:" +
          str(get_response_body['code']))
