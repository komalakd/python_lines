n = int(raw_input("Give a number: "))
result = ['zero not prime'] if n == 0 else [i for i in range(2,n) if n % i == 0]
print 'Not prime!' if len(result) else 'Prime!'
