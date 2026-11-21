favorite_place = {
    'john' : ['japan', 'united states'],
    'ryan' : ['singapre', 'china', 'korea'],
    'pete' : ['brazil']
}

for name, fav_places in favorite_place.items():
    print (f'\n{name.title()}\'s favorite places are: ')
    for places in fav_places:
        print (f'\t{places.title()}')
