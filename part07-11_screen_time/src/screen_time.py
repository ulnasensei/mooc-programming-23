from datetime import datetime, timedelta


filename = input("Filename: ")
start_date_str = input("Start date: ")
amount_days = int(input("How many days: "))

open(filename, "w").close()

start_date = datetime.strptime(start_date_str, "%d.%m.%Y")

data = {}

print("Please type in screen time in minutes on each day (TV computer mobile):")
for i in range(amount_days):
    date_str = datetime.strftime(start_date + timedelta(days=i), "%d.%m.%Y")
    data[date_str] = [int(x) for x in input(f"Screen time {date_str}: ").split()]


total = sum([sum(x) for x in data.values()])
average = total / amount_days
with open(filename, "a") as file:
    file.write(
        f'Time period: {datetime.strftime(start_date, "%d.%m.%Y")}-{datetime.strftime(start_date + timedelta(days=amount_days-1), "%d.%m.%Y")}\n'
    )
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {average}\n")
    for date, minutes in data.items():
        file.write(f'{date}: {"/".join([str(x) for x in minutes])}\n')

print(f"Data stored in file {filename}")
