from faker import Faker

fake = Faker()

while(True):
    print(fake.name())
    print(fake.email())
    print(fake.country())
    print(fake.profile())
