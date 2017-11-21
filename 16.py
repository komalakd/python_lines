import random
import string

def get_valid_chars():
	string_types = [string.lowercase, string.uppercase, string.punctuation]
	return ''.join(string_types)

def strong_psw(length=10):
	valid_chars = get_valid_chars()
	psw = [get_new_char(valid_chars) for i in range(0,length)]
	
	return ''.join(psw)

def weak_psw(length=15,max_words=3):
	some_words = get_some_words()
	qtt_words = random.randint(1,max_words)
	words = [some_words[random.randint(0,len(some_words)-1)] for i in range(0,qtt_words)]
	
	return ''.join(words)

def get_new_char(valid_chars):	
	index = random.randint(0,len(valid_chars))
	return valid_chars[index-1]

def get_some_words():
	return ['andres','esteban','valle','argentina','perro','rosario','laprida']

print 'weak_psw: ' + weak_psw()
print 'strong_psw: ' + strong_psw()
