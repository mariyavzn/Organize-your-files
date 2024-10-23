import csv

from faker import Faker
from random import Random


fieldnames = ['name', 'hiring_date', 'department', 'birthday']
departments = ["HR", 'Marketing', 'Accounting', 'Operations', 'IT']


def get_random_deparment():
    random_index = random.randint(0, len(departments) - 1)
    return departments[random_index]


def create_random_employee(fake: Faker):
    return {fieldnames[0]: fake.name(),
            fieldnames[1]: fake.date_this_decade(),
            fieldnames[2]: get_random_deparment(),
            fieldnames[3]: fake.date_of_birth(minimum_age=18, maximum_age=67)}


with open('employee_records.csv', 'w', newline='') as csvfile:
    fake = Faker()
    random = Random()
    employees_count = random.randint(20, 50)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(employees_count):
        writer.writerow(create_random_employee(fake))
