lists = ['khagaborazi', 'ayarwady', 'singapore', 'yangon', 'burmese', 'toyota']

# Indexing 
print (lists)
print (lists[3].title())
print (lists[1:4])
print (lists[0:6:2])
print (lists[::-1])
print (lists[-1:-4])

message = f'My favorite country is {lists[2].title()}.'
print (message)

# Modifying Elements in a list

print (lists)

lists[0] = 'nile'
print (lists)

# adding elements to a list
 # appending elements to the end of a list

lists.append('bugati')
print (lists)

# inserting elements into a list

print (lists)
lists.insert(0, 'amazon')
print (lists)

# removing elements from a list
    # removing an item using the del statement

lists2 = ['bugati', 'farri', 'lambogini', 'auston martin']
print (lists2)

# del lists2[1]
# print (lists2)

    # removing an item using the pop() Method

print (lists2)

popped_item = lists2.pop()
print (popped_item)

popped_item2 = lists2.pop(1)
print (popped_item2)

message2 = f'This car {popped_item2.title()} is too expensive for me!!'
print (message2)


# removing an item by value

lists2 = ['bugati', 'farri', 'lambogini', 'auston martin']
print (lists2)

lists2.remove('farri')
print (lists2)

luxury_car = 'auston martin'
lists2.remove(luxury_car)
print (lists2)
print (f'\nA \'{luxury_car.title()}\' is too expensive for me.')



# sorting 
lists3 = ['bugati', 'farri', 'lambogini', 'auston martin'.title()]

print ('Here is sorted lists')
print (sorted(lists3))

print ('\n Here is orginal lists')
print (lists3)

print ('\n Here is sort lists with reverse')
lists3.sort(reverse=True)

print ('\n This list is sort lists with reverse')
print (lists3)

print ('Here is sort lists and changed permanently')
lists3.sort()

print ('This list is permanently changed.')
print (lists3)

# reverse order

print ('This is orginal list')
print (lists3)

print ("This is reversed list")
lists3.reverse()
print (lists3)

print (len(lists3))

print (f'This list has {len(lists3)} elements.')