from faker import Faker
# Create an instance of the Faker class
fake = Faker()
# Generate a fake South African cellphone number
# south_african_cellphone_number = fake.phone_number()
south_africa_mobile_number = "+27" + fake.msisdn()[3:]
# Print the generated South African cellphone number
#print("Fake South African Cellphone Number:", south_african_cellphone_number)
print(south_africa_mobile_number)