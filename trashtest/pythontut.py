from curses.ascii import isdigit


while 1:
	num1, operator, num2  = input("Enter your equation: ").split()
	if num1.isdigit() and num2.isdigit():
		num1 = int(num1)
		num2 = int(num2)

		if operator == '+':
			sum = num1 + num2
			print(f"{num1} + {num2} = {sum}")

		elif operator == '-':
			diff = num1 - num2
			print(f"{num1} - {num2} = {diff}")

		elif operator == '*':
			mult = num1 * num2
			print(f"{num1} * {num2} = {mult}")

		elif operator == '/':
			divide = num1 / num2
			print(f"{num1} / {num2} = {divide}")

		elif operator == '%':
			modulus = num1 % num2
			print(f"{num1} % {num2} = {modulus}")

		else:
			print("use +, -, *, /, % next time (in this format: x + y)")
	else:
		print("use +, -, *, /, % next time (in this format: x + y)")
