my_pizza_names = ['seafood pizza', 'chicken pizza', 'cheese pizza']
print (my_pizza_names)

friend_pizza_names = my_pizza_names[:]
print (friend_pizza_names)

my_pizza_names.append('salad pizza')
friend_pizza_names.append('meat pizza')

print (f'My pizza are : ')
for pizza in my_pizza_names:
    print (pizza.title())

print ('Friend pizza are : ')
for pizza in friend_pizza_names:
    print (pizza.title())