import random

beats = {
	'rock': 'scissors',
	'paper': 'rock',
	'scissors': 'paper',
}

def get_symbol():
	word = raw_input("rock, paper or scissors? ")	
	if word in beats.keys():
		return word
	else:
		return get_symbol()

def get_random_symbol():
	return beats.keys()[random.randint(0,2)]

def game():
	human = get_symbol()
	cpu = get_random_symbol()
	
	print 'CPU chose ' + cpu

	if human == cpu:
		print 'TIE!'
		game()
	elif beats[cpu] == human:
		print 'CPU wins!'
	else:
		print 'Human wins!'

game()