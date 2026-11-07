# Test for equality and inequality with strings

car = 'Toyota'

print (f'Is car == "Toyota"? I predict True.')
print (car == 'Toyota')

print (f'Is car == "Honda"? I predict False.')
print (car == 'Honda')

print (f'Is car != "Honda"? I predict True.')
print (car != 'Honda')

print (f'Is car != "Toyota"? I predict False.')
print (car != 'Toyota')

# Test using the lower() method 

print (f'Is car.lower() == "toyota"? I predict True.')
print (car.lower() == 'toyota')

print (f'Is car.lower() == "honda"? I predict False.')
print (car.lower() == 'honda')

# Numerical tests involving equality and inequality, greater than less than, greater than or equal to , and less than or equal to

numbers = 10

print (f'Is numbers == 10? I predict True.')
print (numbers == 10)

print (f'Is numbers != 10? I predict False.')
print (numbers != 10)

print (f'Is numbers > 5? I predict True.')
print (numbers > 5)

print (f'Is number < 6? I predict False.')
print (numbers < 6)

print (f'Is numbers >= 10? I predict True.')
print (numbers >= 10)

print (f'Is numbers <= 9? I prdict False.')
print (numbers <= 9)

# Tests using the and keyword and the or keyword

num = 30

print (f'Is num == 30 and num > 15? I predict True.')
print (num == 30 and num > 15)

print (f'Is num <= 32 or num > 70? I predict True.')
print (num <= 32 or num > 70)

# Test whether an item is in a list

items = ['apple', 'banana', 'cherry']

print (f'Is "apple" in the list? I predict True.')
print ('apple' in items)

print (f'Is "wood" in the list? I predict False.')
print ('wood' in items)


# Test whether an item is not in a list

print (f'Is "apple" not in the list? I predict False.')
print ('apple' not in items)

print (f'Is "wood" not in the list? I predict True.')
print ('wood' not in items)