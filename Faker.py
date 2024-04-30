from datetime import datetime

from faker import Faker
import random
fake = Faker()
fullname = fake.name()
south_african_cellphone_number = fake.phone_number()
name = fullname.split()[0]

   #Generate five random numbers
random_numbers = random.randint(1, 10000000)
print("Random numbers:", random_numbers)
username = name +"_"+str(random_numbers)
print(username)
print("Fake South African Cellphone Number:", south_african_cellphone_number)
#current_time = datetime.now().strftime('%H:%M:%S')
#print(current_time)

