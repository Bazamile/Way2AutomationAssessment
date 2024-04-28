from datetime import datetime

from faker import Faker
import random

fake = Faker()
username = fake.name()
name = username.split()[0]

# Generate five random numbers
random_numbers = random.randint(1, 10000000)
print("Random numbers:", random_numbers)
username = name + "_" + str(random_numbers)
print(username)
# #current_time = datetime.now().strftime('%H:%M:%S')
# #print(current_time)
