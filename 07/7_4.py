
def common_elements():
	list1 = []
	list2 = []
	for i in range(100):
		if i % 3 == 0:
			list1.append(i)
		if i % 5 == 0:
			list2.append(i)
	return set(list1).intersection(set(list2))

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
