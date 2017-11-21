import datetime

name = raw_input("Give me your name: ")
age = raw_input("Give me your age: ")
year = int(datetime.datetime.now().year) + 100 - int(age)

print(name + " will turn 100 years old on " + str(year) + "!")
