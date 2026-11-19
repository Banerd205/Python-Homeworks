information = {
    'amazon river' : 'brazil',
    'ayawadi river' : 'myanmar',
    'nile' : 'egypt'
}

for river, country in information.items():
    print (f'{river.capitalize()} runs through {country.capitalize()}')

for river in information.keys():
    print (f'\n{river.title()}')

for country in information.values():
    print (f'\n{country.title()}')