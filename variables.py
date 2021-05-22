from faker import Faker
fake = Faker()

fake_name = fake.name()
fake_email = fake.email()

# Insert VARIABLES here #
AUTH = "b23d56310020fcd29ea38fb9426ff3d7c7fffa22af8475a53909a23aa50549d8"
payload = {'name': fake_name, 'gender': 'Male', 'email': fake_email, 'status': 'Active'}
