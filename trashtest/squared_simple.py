def square_matrix_simple(matrix=[]):
	squared_values = []

	for line in matrix:
		squared_values.append([c**2 for c in line])

	return squared_values