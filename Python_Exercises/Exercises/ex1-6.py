sec = input("Enter number of seconds:") # enter a numeric value representing a duration in seconds.
sec = int(sec) # conversion from a string to an integer

dd = sec // (24 * 60 * 60) # calculates the number of days in the given duration by performing integer division of the input value by the number of seconds in a day (24 hours * 60 minutes * 60 seconds). 
sec_left = sec - dd * (24 * 60 * 60) # subtracts the number of seconds equivalent to dd days from the initial input.
hh = sec_left // (60*60)
sec_left = sec_left % (60*60) # calculates the number of hours in the remaining seconds by performing integer division by the number of seconds in an hour (60 minutes * 60 seconds). 
mm = sec_left // 60 # calculates the number of minutes in the remaining seconds by performing integer division by the number of seconds in a minute (60 seconds)
sec_left = sec_left % 60 # calculates the remaining seconds after extracting the minutes by taking the modulus of the remaining seconds with 60 (the number of seconds in a minute).

print(dd)
print(hh)
print(mm)
print(sec_left)

print(f"{dd} : {hh} : {mm} : {sec_left}")