fav_numbers = {
    'emma' : 7,
    'emily' : 20,
    'john' : 60,
    'peter' : 40,
    'banerd' : 20
}

num = fav_numbers['emma']
print (f"\nEmma's favorite number is {num}")

num = fav_numbers['emily']
print (f"Emily's favorite number is {num}")

num = fav_numbers['john']
print (f"John's favorite number is {num}")

num = fav_numbers['peter']
print (f"Peter's favorite number is {num}")

num = fav_numbers['banerd']
print (f"Banerd's favorite number is {num}\n")

for name, fav_number in fav_numbers.items():
    print (f'{name.title()}\'s favorit number is {fav_number}.')
