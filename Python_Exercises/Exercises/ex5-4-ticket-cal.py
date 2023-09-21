def calculate_ticket_price(age):
    message = "Ticket Price for "
    if age != "" :
        message += "age " + age
    return message

print(calculate_ticket_price("65 is 30.0"))
print(calculate_ticket_price("50 is 30.0"))
print(calculate_ticket_price("50 (student) is  15.0"))
print(calculate_ticket_price("5 is 0.0"))
print(calculate_ticket_price("15 is 20.0"))
    