cities = {
    'myitkyina' : {
        'country' : 'myanmar',
        'population' : '9 million',
        'fact' : 'There are alot of beautiful temples, church and places'
    },
    'tokyo' : {
        'country' : 'japan',
        'population' : '45 million',
        'fact' : 'It has the busiest rail netword in the world.'
    },
    'silicon valley' : {
        'country' : 'united states',
        'population' : '55 million',
        'fact' : 'Most of tech giant company are there!'
    }
}

# cities['myitkyina'] ['area'] = '150,453 sq km'
cities['silicon valley'] ['area'] = '2,653,589 sq km'
cities['tokyo'] ['area'] = '2,234,322 sq km'

for city, cities_infos in cities.items():
    country = f'{cities_infos['country'].title()}'
    population = f'{cities_infos['population']}'
    fact = f'{cities_infos['fact']}'
    # area = f'{cities_infos['area']}'

    print (f'\nCity: {city.title()}')
    print (f'\tCountry: {country.title()}')
    print (f'\tPopulation: {population}')
    print (f'\tFact: {fact.title()}')
    # print (f'\tArea: {area}')

    if 'area' in cities_infos:
        print (f'\tArea: {cities_infos['area']}')
    else:
        print (f'\tArea: not availiable yet')
