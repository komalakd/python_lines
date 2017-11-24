def get_input(number):
	cond = raw_input(str(number)+'? ')
	if cond not in ['higher','lower','ok']:
		return get_input()
	return cond

min_ = 1
max_ = 99

while True:
	num = (max_ - min_) / 2 + min_
	status = get_input(num)

	if status == 'higher':
		min_ = num
	elif status == 'lower':
		max_ = num
	else:
		print 'Got it!'
		break
		