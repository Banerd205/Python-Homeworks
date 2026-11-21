responses = {}
polling_active = True
prompt = 'If you could visit one place in the world, where would you go?: '

while polling_active:
    name = input('\nEnter your name: ')
    fav_place = input(prompt).strip().title()
    responses[name] = fav_place

    repeat = input('Would you like to let another person respond? "yes" or "no": ')
    if repeat == 'no':
        print ('Thanks')
        polling_active = False

print ("\n--- Dream Vacation Poll Results ---")
for name, place in responses.items():
    print (f"\t{name}'s favorite place is {place}.")