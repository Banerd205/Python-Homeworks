five_words = {
    'variable' : 'variable is a box to store temporary value which can change later.',
    'string' : 'a series of characters representing text.',
    'int' : 'int is a data type/constructor for whole numbers, rather than a function that solves all math problems.',
    'loop' : 'a way to repeat a block of code multiple times.',
    'dictionary' : 'dictionary\'s function is storing key - value pairs.'
}

five_words['set'] = 'set is to store a bunch of data like list'
five_words['float'] = 'float\'s function is manipulation math problem but it is decimal'
five_words['if codition'] = 'if condition\'s function is checking situations.'
five_words['input'] = 'the function of Input is requesting information from users.'
five_words['list'] = 'list store a bunch of information'

# print (five_words)

for word, meaning in five_words.items():
    print (f'\n{word}: ')
    print (f'\t{meaning}.')