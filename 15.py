def reverse_word(phrase='My name is Michele'):
	words = phrase.split(' ')
	print words

	l_reversed = words[::-1]
	#l_reversed = reversed(words) # iterator???
	print l_reversed

	done = ' '.join(l_reversed)
	print done

reverse_word()