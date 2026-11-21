five_words = {
    'variable' : 'variable is a box to store temporary value which can change later.',
    'string' : 'a series of characters representing text.',
    'int' : 'int is a data type/constructor for whole numbers, rather than a function that solves all math problems.',
    'loop' : 'a way to repeat a block of code multiple times.',
    'dictionary' : 'dictionary\'s function is storing key - value pairs.'
}

word = 'variable'
print (f"\n{word.title()}: \n\t{five_words['variable']}")

word = 'string'
print (f"{word.title()}: \n\t{five_words['string']}")

word = 'int'
print (f"{word.title()}: \n\t{five_words['int']}")

word = 'loop'
print (f"{word.title()}: \n\t{five_words['loop']}")

word = 'dictionary'
print (f"{word.title()}: \n\t{five_words['dictionary']}\n")


for word, meaning in five_words.items():
    print (f'{word.title()}: ')
    print (f'\t{meaning.capitalize()}\n')