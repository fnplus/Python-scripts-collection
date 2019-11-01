from datetime import datetime, timedelta


user_input = input("pick a year ")

while not user_input.isdigit():
    print("Please enter a year.")
    user_input = input("pick a year ")

currently_read = start_datetime = datetime(int(user_input), 1, 1, 0, 0, 0)
end_datetime = datetime(int(user_input), 12, 31, 0, 0, 0)
difference = end_datetime - start_datetime

while currently_read < end_datetime:
    print((currently_read + timedelta(days=1)).strftime("%Y-%m-%d"),)

    currently_read += timedelta(days=1)
