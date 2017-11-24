from sets import Set
import random

def get_numeric_string(length=4):
	return str(random.randint(0,9999)) #random 4 digit number

def guess(the_string, guessing, tree):
	
	if the_string == guessing:
			return True
		
	cows = 0
	bulls = 0
	
	for i, x in enumerate(guessing):
		if tree.get(x):
			if i in tree.get(x):
				cows += 1
			else:
				bulls += 1
		i += 1


	print 'Cows: ' + str(cows)
	print 'Bulls: ' + str(bulls)

	return False

def get_input_number():
	while True:
		guessing = raw_input('Enter a number: ')
		if len(guessing) == 4:
			return guessing

def new_tree(the_string):

	tree = {}
	for i, x in enumerate(the_string):
		if tree.get(x):
			tree[x].append(i)
		else:
			tree[x] = [i]
		i += 1

	return tree

def main():
	the_string = get_numeric_string()

	tree = new_tree(the_string)

	count = 1
	while True:
		guessing = raw_input('Enter a number: ')
		if guess(the_string, guessing, tree):
			print 'Correct! Number of guesses: ' + str(count)
			break
		else:
			count += 1

main()