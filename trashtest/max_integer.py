def max_integer(my_list=[]):
	if not my_list:
		return None
	if my_list:
		my_list.sort()
		return my_list[-1]
	# else:
	# 	for i in my_list:
	# 		if my_list[i] > my_list[i + 1]:
	# 			max = my_list[i]
	# 		else:
	# 			max = my_list[i + 1]
	# return max