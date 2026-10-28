fruits = ['apple', 'mango', 'lemon', 'banana', 'grapes']

print ('The first three fruits are: ')

for fruit in fruits[:3]:
    print (fruit.title())

print ('Three items from the middle of the list are: ')

for fruit in fruits[1:4]:
    print (fruit.title())

print ('The last three items in the list are: ')

for fruit in fruits[-3:]:
    print (fruit.title())


cube_lists = [number ** 3 for number in range(1, 11)]
print (cube_lists)

print ('The first three items in the list are : ')
print (cube_lists[:3])

print ('Three items from the middle of the list are : ')
print (cube_lists[1:4])

print ('The last three items in the list are : ')
print (cube_lists[-3:])