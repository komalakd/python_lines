import random
from sets import Set

def get_list(min_len=5,max_len=10,min=1,max=10):
	qtt = random.randint(min_len, max_len)

	list = []
	for x in xrange(0,qtt):
		list.append(random.randint(min, max))
	return list

def diff_set(l1,l2):
	return list(Set(l1).difference(Set(l2)))

def diff_dict(l1,l2):
	diff = {}
	dict_2 = list_to_dict(l2)
	
	for i in l1:
		if not dict_2.get(i):
			diff[i] = 1
	
	return diff.keys()

def diff_list(l1,l2):
	l = []
	for i in l1:
		i_not_in_l2 = True
		for j in l2:
			if i == j:
				i_not_in_l2 = False
				break
		if i_not_in_l2:
			l.append(i)
	return list(Set(l))

def list_to_dict(l,value=1):
	return dict((key,value) for key in l)

def main():
	l1 = get_list()
	l2 = get_list()

	print l1
	print l2
	print diff_set(l1,l2)
	print diff_dict(l1,l2)
	print diff_list(l1,l2)

main()
