def no_c(my_string):
	new_string = ""
	for elements in my_string:
		if elements != 'C' and elements != 'c':
			new_string += elements
	return new_string