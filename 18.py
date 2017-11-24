from sets import Set
import random

def get_numeric_string(length=4):
	
	numeric_string = ''
	for i in xrange(1,length+1):
		digit = random.randint(0,9)
		numeric_string += str(digit)

	return numeric_string

def guess(the_string, guessing, tree):
	
	if the_string == guessing:
		return True
		
	cows = 0
	bulls = 0
	i = 0
	print tree
	for x in guessing:
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
	i = 0
	for x in the_string:
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