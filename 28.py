def max_number(a,b,c):
	solution_1(a,b,c)
	solution_2(a,b,c)

def solution_1(a,b,c):
	if a > b:
		if a > c:
			print a
		elif c > b:
			print c
		else:
			print b
	elif b > c:
		print b
	else:
		print c

def solution_2(a,b,c):
	if a >= b and a >= c:
		print a
	if b >= a and b >= c:
		print b
	if c >= a and c >= b:
		print c
			

if __name__ == '__main__':
	max_number(2,5,8)
	max_number(2,8,5)
	max_number(5,2,8)
	max_number(5,8,2)
	max_number(8,2,5)
	max_number(8,5,2)
