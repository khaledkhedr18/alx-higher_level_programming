def delete_at(my_list=[], idx=0):
	list_len = len(my_list) - 1
	if idx < 0:
		return my_list
	elif idx > list_len:
		return my_list
	else:
		for i in my_list:
			if i == my_list[idx]:
				my_list.remove(i)
	return my_list