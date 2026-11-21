prompt = 'Enter you age or Enter "quit" to stop.: '
total_ticket = []
total_cost = []

while True:
    user_input = input(prompt).strip()

    if user_input.lower()  == 'quit':
        break

    age = int(user_input)
    total_ticket.append(age)

    if age <= 3:
        print (f"The ticket is free")
    elif age <= 12:
        price = 10
        total_cost.append(price)
        print (f"The ticket will cost ${price}")
    else:
        price = 15
        total_cost.append(price)
        print (f"The ticket will cost ${price}")

total_ticket_qunatity = (len(total_ticket))
total_cost_for_tickets = (sum(total_cost))
print (f"\nTotal ticket: {total_ticket_qunatity}")
print (f"\nTotal price for all tickets: ${total_cost_for_tickets}")