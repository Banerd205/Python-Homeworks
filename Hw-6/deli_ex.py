sandwich_orders = ['tuna', 'club', 'grilled cheese', 'chicken']
finished_sandwichs = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made {current_sandwich} sandwich.")
    finished_sandwichs.append(current_sandwich)

print ("\nThe following sandwich have been made: ")
for sandwich in finished_sandwichs:
    print (f"\t- {sandwich} sandwich.")


# Updated version 

# sandwich_orders = []
# finished_sandwiches = []

# sandwich_orders = input('What kind of sandwich would you order: ').split(', ')

# for sandwich in sandwich_orders:
#     print (f"I made a {sandwich}")
#     finished_sandwiches.append(sandwich)

# print ('\nI made the following sandwich lists: ')
# for sandwich in finished_sandwiches:
#     print (f"\t- {sandwich}")

