import random

number = random.randint(1,10)
hits = 0

def get_number():
	user_input = raw_input("Give a number or type 'exit': ")
	if user_input.lower() == 'exit':
		return 0
	try:
		return int(user_input)
	except:
		get_number()

def game():
	guess = get_number()
	global hits
	if guess == 0:
		print 'You have guessed ' + str(hits) + ' times!'
	elif guess > number:
		print 'Too high!'
		game()
	elif guess < number:
		print 'Too low'
		game()
	else:
		hits = hits + 1
		print 'Correct!'
		game()

game()