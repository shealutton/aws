from faker import Faker


factory = Faker()

for i in range(10):
    first = factory.first_name()
    last = factory.last_name()
    age = factory.random.randrange(18,59)
    print(first, last, age)