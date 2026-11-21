# prompt = '\nEnter a pizza topping you want to add: '

# while True:
#     topping = input(prompt)

#     if topping == 'quit':
#         break
#     else:
#         print (f'I will add {topping} for your pizza')


# Updated version 

# create promt variable and empty topping lists
prompt = "\nEnter a pizza topping you want to add: "
toppings = []

while True:
    topping = input(prompt).strip()
    # checking the user input whether quit or add
    if topping.lower() == 'quit':
        break
    
    # add new topping adding by user to toppings empty list
    toppings.append(topping)
    print (f"I'll add {topping} to your pizza.")

#check whether the user's toppings are in the toppings list
if toppings:
        print ("\nYour pizza will have these topings: ")

        for topping in toppings:
            print (f"\t{topping}")
else:
    print ("You did not add any pizza toppings.")

