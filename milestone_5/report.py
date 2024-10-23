import csv
import sys
from datetime import datetime

from generate_data import fieldnames


def read_csv(file_name: str):
    employee_list = []
    with open(file_name, mode='r') as file:
        csvFile = csv.reader(file)
        first_line_skip = True
        for lines in csvFile:
            if first_line_skip:
                first_line_skip = False
                continue

            employee = {}
            employee[fieldnames[0]] = lines[0] # name
            employee[fieldnames[1]] = datetime.strptime(lines[1], '%Y-%m-%d') # hiring_date
            employee[fieldnames[2]] = lines[2] # department
            employee[fieldnames[3]] = datetime.strptime(lines[3], '%Y-%m-%d') # birthday
            employee_list.append(employee)

    return employee_list


csv_file_arg = sys.argv[1]
month_arg = sys.argv[2]

employee_list = read_csv(file_name=csv_file_arg)
entered_date = datetime.strptime(month_arg[0].upper() + month_arg[1:].lower(), "%B")


anniversaries_count = 0
anniversaries_by_departments = {}
birthdays_count = 0
birthdays_by_departments = {}

for employee in employee_list:
    hiring_date: datetime = employee['hiring_date']
    if hiring_date.month == entered_date.month:
        anniversaries_count += 1
        employee_department = employee['department']
        if employee_department in anniversaries_by_departments:
            anniversaries_by_departments[employee_department] += 1
        else:
            anniversaries_by_departments[employee_department] = 1

    birthday: datetime = employee['birthday']
    if birthday.month == entered_date.month:
        birthdays_count += 1
        employee_department = employee['department']
        if employee_department in birthdays_by_departments:
            birthdays_by_departments[employee_department] += 1
        else:
            birthdays_by_departments[employee_department] = 1


print('Report for April generated')
print('--- Birthdays ---')
print(f'Total: {birthdays_count}')
print('By department:')
for department, birthdays in birthdays_by_departments.items():
    print(f' - {department}: {birthdays}')

print('\n')

print('--- Anniversaries ---')
print(f'Total: {anniversaries_count}')
print('By department:')
for department, anniversaries in anniversaries_by_departments.items():
    print(f' - {department}: {anniversaries}')