#version 1: Use a conditional test in the while statement to stop the while loop
prompt = "\nEnter a pizza topping (or enter 'quit' to finish): "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print (f'Adding {topping} to your pizza!')
    

# version 2: Use an active variable to control how long the loop run

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print (f'Adding {topping} to your pizza!')
    

# version 3: use a break statement to exit the loop

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print (f'Adding {topping} to your pizza')


# greeting = ("Hello, welcome")
# registered_user = ['merry', 'lulu', 'emily', 'emma', 'ryan', 'peter']

# print (greeting)

# while True:
#     user_input = input("Enter username (or 'quit' to exit): ").lower().strip()

#     if user_input == 'quit':
#         print ('Goodbye!')
#         break

#     if not user_input:
#         print ("Username cannot be empty")
#         continue

#     if user_input in registered_user:
#         print (f"{user_input} is not available, enter a different one.")
#         continue
#     else:
#         print (f"Great! Welcome, {user_input}")
#         password = input("Enter password: ").strip()
#         if password:
#             print(f"Great! {user_input}, you create an account")
#             break
#         else:
#             print ("Password cannot be empty. Please try again.")
            
        


