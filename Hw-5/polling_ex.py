favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

peoples_to_poll = ['merry', 'sarah', 'peter', 'phil']

for person in peoples_to_poll:
    if person in favorite_languages:
        print (f'Thank you, {person.title()} has alrady polled.')
    else:
        print (f'{person.title()} has not taken survey yet!')
    