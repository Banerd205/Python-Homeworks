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

for city, city_infos in cities.items():
    country = city_infos['country'].title()
    population = city_infos['population']
    fact = city_infos['fact']

    print (f'\nCity: {city.title()}')
    print (f'\tCountry: {country}.title()')
    print (f'\tPopulation: {population}')
    print (f'\tFact: {fact}')   

    # print (f'\nCity: {city.title()}')
    # print (f'\tCountry: {city_infos['country'].title()}')
    # print (f'\tPopulation: {city_infos['population'].title()}')
    # print (f'\tFact: {city_infos['fact']}')