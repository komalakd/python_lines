n = int(raw_input("give a number: "))
print('-'.join(map(lambda x: str(x), filter(lambda x: x > n, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))))

# for singular in [element for element in [1,1,2,3,6,8,13,21,34,55,89] if element < 5]: print(singular)


