info1 = {
    'first_name' : 'Tylor',
    'last_name' : 'Swift',
    'city' : 'New York'
}

info2 = {
    'first_name' : 'Peter',
    'last_name' : 'Packer',
    'city' : 'los angle'
}

info3 = {
    'first_name' : 'Ryan',
    'last_name' : 'Rynold',
    'city' : 'silicon valley'
}

peoples = [info1, info2, info3]

for people in peoples:
    full_name = f'{people['first_name'].title()} {people['last_name'].title()}'
    city = f'{people['city'].title()}'
    print (f'{full_name} lives in {city}')
