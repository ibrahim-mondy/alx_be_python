from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")
display_current_datetime()

user = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date():
    future_date = datetime.now() + timedelta(days = user)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

calculate_future_date() 