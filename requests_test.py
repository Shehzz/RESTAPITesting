import pytest
import requests
import json

AUTH = "b23d56310020fcd29ea38fb9426ff3d7c7fffa22af8475a53909a23aa50549d8"

def test_checking_for_200_status():
    response = requests.get("https://gorest.co.in/public-api/users/")
    assert response.status_code == 200


def test_checking_for_deleted_user():
    get_response_body = requests.get("https://gorest.co.in/public-api/users/12341111").json()
    assert get_response_body['code'] == 404
    print("The HTTP response code received is:" + str(get_response_body['code']))


# Verifying the body of the response headers
def test_check_content_type_equals_json():
    response = requests.get("https://gorest.co.in/public-api/users/")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_creating_a_new_user_using_POST_123():
    auth_header = {'Authorization': 'Bearer '+AUTH}
    payload = {'name': 'SM 123', 'gender': 'Male', 'email': 'abb16677722@123.com', 'status': 'Active'}
    response = requests.post("https://gorest.co.in/public-api/users/", headers=auth_header, data=payload)
    response_json = response.json()
    #print(response_json['data']['id'])
    global response_id # Change this to a fixture for later use
    response_id = response_json['data']['id']
    print("The userID generated is:" + str(response_id))
    assert response_json['code'] == 201

def test_checking_for_same_existing_user_123():
    response = requests.get("https://gorest.co.in/public-api/users/" + str(response_id)).json()
    assert response['code'] == 200
    print("The HTTP response code received is:" + str(response['code']))
