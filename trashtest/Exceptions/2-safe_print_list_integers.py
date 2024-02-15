def safe_print_list_integers(my_list=[], x=0):
	try:
		realnum = 0
		for i in range(x):
			if isinstance(my_list[i], int):
				print("{:d}".format(my_list[i]), end = "")
				realnum += 1
	except (IndexError):
		pass
	print()
	return realnum