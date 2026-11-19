fav_numbers = {
    'emma' : [7, 20, 30, 77, 70],
    'emily' : [20, 24, 56],
    'john' : [60, 56, 76, 3],
    'peter' : [40, 4],
    'banerd' : [20, 80, 90, 1002]
}

for name, numbers in fav_numbers.items():
    print (f'\n{name.title()}\'s favorite numbers are: ')
    for number in numbers:
        print (f'\t- {number}')
