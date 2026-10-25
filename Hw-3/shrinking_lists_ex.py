print ('I have only 2 seats for dinner')

guest_lists = ['Ryan', 'Mary', 'Misha', 'Peter', 'Emma', 'John']

popped_guests = []
invited_guests = []

popped_guests.append(guest_lists.pop(0))
popped_guests.append(guest_lists.pop(2))
popped_guests.append(guest_lists.pop(2))
popped_guests.append(guest_lists.pop(2))

invited_guests.append(guest_lists[0])
invited_guests.append(guest_lists[1])

print ('Popped Guest Lists')
print (popped_guests)

print ('Invited Guests')
print (invited_guests)

print (f'Hello {popped_guests[0]}, I am sorry to inform you that you are no longer in the invition list !')
print (f'Hey {popped_guests[1]}, You have been dislist for upcoming dinner party')
print (f'Hi {popped_guests[2]} is in the popped list')
print (f'{popped_guests[3]} is in the removed list')

print (f'{invited_guests[0]} is still on the list')
print (f'{invited_guests[1]} is still on the list')

for popped_guest in popped_guests:
    print (f'Hi \"{popped_guest}\", You are no longer in the list for upcoming dinner party.')

for invited_guest in invited_guests:
    print (f'Hi {invited_guest}, you are still on the list for upcoming dinner party.')

print (guest_lists)

del guest_lists[0]
del guest_lists[0]
print (guest_lists)