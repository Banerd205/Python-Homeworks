# current_users = ['admin', 'van', 'james', 'banerd', 'merry']
# new_users = ['mary', 'merry', 'banerd', 'jarome', 'ryan']

# current_users_lower = [user.lower() for user in current_users]

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print (f'Sorry, "@{new_user}" is already taken. Please enter a new username,')
#     else:
#         print (f'"@{new_user}" is available.')



current_users = ['admin', 'van', 'james', 'banerd', 'merry']
current_users_lower = [user.lower() for user in current_users]

while True:

    is_got_username = False
    new_users = input('Enter new usernames: ').lower().split(', ')
        
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print (f'Sorry, "@{new_user}" is already taken.')
        else:
            print (f'"@{new_user}" is available.')
            is_got_username = True
    if is_got_username:
        print (f'Welcome {new_user}')
        break
