from faker import Faker
fake = Faker()

"""Faker library is used to auto-generate name and email attributes that are being used in the payload"""

fake_name = fake.name()
fake_email = fake.email()

fake_name2 = fake.name()
fake_email2 = fake.email()

"""Insert VARIABLES here"""

# AUTH is used for performing POST/PUT/DELETE actions
AUTH = "b23d56310020fcd29ea38fb9426ff3d7c7fffa22af8475a53909a23aa50549d8"

# payload is the data that is being sent in the POST request method
payload = {'name': fake_name, 'email': fake_email, 'gender': 'Male', 'status': 'Active'}

# updated_payload is the data that is being sent in the PUT request method
updated_payload = {'name': fake_name2, 'email': fake_email2, 'gender': 'Male', 'status': 'Active'}

# faulty_payload is the data that is being sent to check how the API responds to incomplete data
faulty_payload = {'name': 'ABC ABC', 'gender': 'Male', 'status': 'Inactive'}

# nonexistent_user is used to check how the API reacts to failed GET request
nonexistent_user = "123123"
