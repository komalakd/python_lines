import random
from sets import Set

def get_list(min_len=5,max_len=10,min=1,max=10):
	qtt = random.randint(min_len, max_len)

	list = []
	for x in xrange(0,qtt):
		list.append(random.randint(min, max))
	return list

def remove_duplicates_set(l):
	return list(Set(l))

def remove_duplicates_list(l):
	return list_to_dict(l).keys()

def list_to_dict(l,value=1):
	return dict((key,value) for key in l)

def main():
	l = get_list()

	print l
	print remove_duplicates_set(l)
	print remove_duplicates_list(l)

main()
