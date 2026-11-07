age = 2

if age < 2:
    print ('The person is a baby.')
elif age >= 2 and age < 4:
    print ('The person is a toddler.')
elif age >= 4 and age < 13:
    print ('The person is a kid.')
elif 13 <= age < 20:
    print ('The person is a teenager.')
elif 20 <= age < 65:
    print ('The person is an adult.')
else:
    print ('The person is an elder.')