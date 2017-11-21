###in operator
### using a key to get a value
# create a dictionary of terms

terms = {'variable' : 'represents or refers to a value stored in memory','string' : 'A sequence of characters'};

if 'float' in terms:
	print("I know what a float is.")
else:
	print("I do not know what that is.")
print(terms['variable']) 