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

number = int(raw_input("Give a number: "))
print fibonacci(number)
print serie
