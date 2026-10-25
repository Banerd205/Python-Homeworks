guest_lists = ['Mary', 'Peter', 'John']

print (f'Hey, {guest_lists[0]} I just added three more new seats. So I will invite three more people.')

guest_lists.insert(0, 'Ryan')
guest_lists.insert(2, 'Misha')
guest_lists.append('Emma')

print (f'Hello {guest_lists[0]}, Can you come and join our dinner party?')
print (f'Hi {guest_lists[2]}, Come and join our dinner party!!')
print (f'Hey {guest_lists[5]}, Come and join our dinner party!')