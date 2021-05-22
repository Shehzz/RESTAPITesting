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

    # global response_id  # TODO Change this to a fixture/global for later use

    response_id = response_json['data']['id']
    pytest.global_response_id = response_id  # making the response_id a GLOBAL variable
    print("\nThe userID generated is:" + str(response_id))
    assert response_json['code'] == 201, "The HTTP response code is not 201"
    assert data_verification(URL)


@pytest.mark.parametrize(
    "name, email, gender, status",
    [
        (variables.fake_name, variables.fake_email, "Male", "Active")
    ]
)
def test_data_verification_method(URL, name, email, gender, status):
    response = requests.get(URL + str(pytest.global_response_id)).json()
    assert response['data']['id'] == pytest.global_response_id
    assert response['data']['name'] == name
    assert response['data']['email'] == email
    assert response['data']['gender'] == gender
    assert response['data']['status'] == status
    assert response['code'] == 200
    print("\nThe HTTP response code received is:" + str(response['code']))
    return True


def data_verification(URL):
    response = requests.get(URL + str(pytest.global_response_id)).json()
    if response['data']['id'] == pytest.global_response_id and \
       response['data']['name'] == variables.fake_name and \
       response['data']['email'] == variables.fake_email and \
       response['data']['gender'] == "Male" and \
       response['data']['status'] == "Active":
        print("\nData Validation success!")
        print(response)
        return True
    else:
        print("\nData Validation failed!")
        return False
