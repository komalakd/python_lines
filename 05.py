from sets import Set
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = {}

for x in a:
	for y in b:
		if x == y:
			c[x] = 1

print c.keys()

qt1 = random.randint(5, 10)
qt2 = random.randint(5, 10)

a2 = []
b2 = []

for x in xrange(0,qt1):
	a2.append(random.randint(1, 15))

for x in xrange(0,qt2):
	b2.append(random.randint(1, 15))

print a2
print b2
print Set(a2).intersection(Set(b2))
