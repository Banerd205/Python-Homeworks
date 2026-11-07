car = 'BMW'

print (f'Is car == "BMW"? I predict True.')
print (car == 'BMW')

print (f'Is car != "Marcedes"? I predict True.')
print (car != 'Marcedes')

print (f'Is car.upper()? I predict True.')
print (car.upper() == 'BMW')

print (f'Is car == "bool"? I predict True.')
print (bool(car))

print (f'Is len(car) == 3? I predict True.')
print (len(car) == 3)

print (f'Is car == "bmw"? I predict False.')
print (car == 'bmw')

print (f'Is len(car) == 5? I predict False.')
print (len(car) == 5)

print (f'Is car .lower() == "bmw"? I predict False.')
print (car.lower() == 'bmw')

print (f'Is len(car) > 10? I predict False.')
print (len(car) > 10)

print (f'Is car == "Audi"? I predict False.')
print (car == 'Audi')