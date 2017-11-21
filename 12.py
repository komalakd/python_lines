a = [5, 10, 15, 20, 25]

def extremos(a):
	return [a[0], a[-1]]

def extremos2(a):
	return a[0:len(a):len(a)-1]

print extremos(a)
print extremos2(a)
