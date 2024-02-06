def uniq_add(my_list=[]):
	new_list = list(set(my_list))

	k = 0
	for i in new_list:
		k += i
	return k