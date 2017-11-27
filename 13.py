serie = {
	0: 0,
	1: 1,
	2: 1,
}

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		serie[n] = fibonacci(n-1) + fibonacci(n-2)
		return serie[n]

def fibonacci_loop(n):
	n1 = 0
	n2 = 1
	for i in range(1,n):
		if n == 1:
			n1 = 0
			n2 = 1
		elif n == 2:
			n1 = 0
			n2 = 1
		else:
			aux = n1 + n2
			n1 = n2
			n2 = aux
	return n1 + n2


number = int(raw_input("Give a number: "))
print fibonacci(number)
print fibonacci_loop(number)
print serie