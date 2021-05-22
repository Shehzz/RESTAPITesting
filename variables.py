from faker import Faker
fake = Faker()

fake_name = fake.name()
fake_email = fake.email()

fake_name2 = fake.name()
fake_email2 = fake.email()

# Insert VARIABLES here #
AUTH = "b23d56310020fcd29ea38fb9426ff3d7c7fffa22af8475a53909a23aa50549d8"
payload = {'name': fake_name, 'email': fake_email, 'gender': 'Male', 'status': 'Active'}
updated_payload = {'name': fake_name2, 'email': fake_email2, 'gender': 'Male', 'status': 'Active'}
faulty_payload = {'name': 'ABC ABC', 'gender': 'Male', 'status': 'Inactive'}
nonexistent_user = "123123"
