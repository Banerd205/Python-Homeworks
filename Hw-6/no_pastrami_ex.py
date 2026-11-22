sandwich_orders = ['pastrami', 'tuna', 'club', 'pastrami', 'grilled cheese', 'pastrami', 'chicken']
finished_sandwichs = []

print ("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print ('\n')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f"I am working on your {current_sandwich} sandwich.")
    finished_sandwichs.append(current_sandwich)

print ('\nThe following sandwich are finished: ')
for sandwich in finished_sandwichs:
    print (f"\t- {sandwich}")