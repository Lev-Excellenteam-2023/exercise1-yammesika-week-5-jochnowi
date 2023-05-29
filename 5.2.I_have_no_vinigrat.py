from datetime import datetime
import random
import time


def generate_random_date(start_date, end_date):
    start_epoch = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
    end_epoch = int(time.mktime(time.strptime(end_date, "%Y-%m-%d")))

    random_epoch = random.randint(start_epoch, end_epoch)
    random_date = time.localtime(random_epoch)
    weekday = time.strftime("%A", random_date)

    return weekday


# User input
start_date = input("Enter the start date (in the format YYYY-MM-DD): ")
end_date = input("Enter the end date (in the format YYYY-MM-DD): ")


weekday = generate_random_date(start_date, end_date)

print(weekday)

if weekday == "monday":
    print("I have no vinigret!")