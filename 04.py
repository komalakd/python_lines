n = int(raw_input("give a number: "))
print('-'.join(map(lambda x: str(x), filter(lambda x: n % x == 0, range(1, n)))))
