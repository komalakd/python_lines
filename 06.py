word = raw_input("give me a word: ")

index_1 = 0
index_2 = len(word) - 1
palindrom = True

while True:
	if word[index_1] != word[index_2]:
		palindrom = False
		break
	elif index_1 > index_2:
		break
	index_1+=1
	index_2-=1

print 'YES' if palindrom else 'NO'

print 'This is a Palindrome' if word[::-1] == word else 'This is NOT a Palindrome'
