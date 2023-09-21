import time

def is_morning(current_time):
    # Extract the hour and minute from the current time
    current_hour, current_minute = map(int, current_time.split(':'))

    # Check if the time is in the morning (before noon)
    if current_hour < 12:
        return True
    else:
        return False

# Get the current time in HH:MM format
current_time = time.strftime("%H:%M")

# Check if it's morning and print a message
if is_morning(current_time):
    print("Good morning!")
