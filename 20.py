a = [1, 3, 5, 30, 42, 43, 500]

num = int(raw_input('Give me a number: '))

min_ = 0
max_ = len(a) - 1

while True:
	
	pos = (max_ - min_) / 2 + min_

	if a[pos] == num:
		print 'Position: ' + str(pos+1)
		break
	elif a[pos] < num:
		if min_ == pos:
			print 'Not found!'
			break
		min_ = pos
	else:
		if max_ == pos:
			print 'Not found!'
			break
		max_ = pos
