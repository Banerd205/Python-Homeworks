pet_1 = {
    'kind' : 'cat',
    'name' : 'milo',
    'age' : 3,
    'owner' : 'Emma'
}
pet_2 = {
    'kind' : 'dog',
    'name' : 'kiwi',
    'age' : '4',
    'owner' : 'emily'
}
pet_3 = {
    'kind' : 'parrot',
    'name' : 'buddy',
    'age' : 2,
    'owner' : 'Ci Ci'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    kind = f'{pet['kind'].title()}'
    name = f'{pet['name'].title()}'
    age = f'{pet['age']}'
    owner = f'{pet['owner'].title()}'
    
    print (f'\n{name}\'s informations: ')
    print (f'\tOwner is {owner}.')
    print (f'\tKind: {kind}')
    print (f'\tAge: {age} years old.')