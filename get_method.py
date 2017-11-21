###using the get() method with a dictionary

terms = {'integer' : 'A whole number.'}

print(terms.get('integer'))
print(terms.get('float', 'Not in the dictionary'))

###editing and deleting values in a dictionary
terms = {'integer' : 'Is a number that contains a decimal place.', 'string' : 'a sequence of characters.'}

terms['integer'] = 'A whole number.'
print(terms.get('integer'))

del terms['integer']
print(terms)