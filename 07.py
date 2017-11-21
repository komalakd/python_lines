a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print filter(lambda x: x % 2 != 0, a)
print [x for x in a if x % 2 != 0]
