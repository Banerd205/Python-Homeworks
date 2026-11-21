greeting = ("Hello, welcome")
registered_user = ['merry', 'lulu', 'emily', 'emma', 'ryan', 'peter']

print (greeting)

while True:
    user_input = input("Enter username (or 'quit' to exit): ").lower().strip()

    if user_input == 'quit':
        print ('Goodbye!')
        break

    if not user_input:
        print ("Username cannot be empty")
        continue

    if user_input in registered_user:
        print (f"{user_input} is not available, enter a different one.")
        continue
    else:
        print (f"Great! Welcome, {user_input}")
        password = input("Enter password: ").strip()
        if password:
            print(f"Great! {user_input}, you create an account")
            break
        else:
            print ("Password cannot be empty. Please try again.")
            
        


