def safe_print_list(my_list=[], x=0):
	try:
		k = 0
		for i in range(x):
			print(my_list[i], end = "")
			k += 1
	except IndexError:
			pass
	finally:
		print()
		return k