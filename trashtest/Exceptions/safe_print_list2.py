def safe_print_list(my_list=[], x=0):
	try:
		realnum = 0
		for i in range(x):
			print(my_list[i], end = "")
			realnum += 1
	except IndexError:
		pass
	print()
	return realnum