five_words = {
    'variable' : 'variable is a box to store temporary value which can change later.',
    'string' : 'a series of characters representing text.',
    'int' : 'int is a data type/constructor for whole numbers, rather than a function that solves all math problems.',
    'loop' : 'a way to repeat a block of code multiple times.',
    'dictionary' : 'dictionary\'s function is storing key - value pairs.'
}

for word, meaning in five_words.items():
    print (f'{word.title()}: ')
    print (f'\t{meaning.capitalize()}\n')