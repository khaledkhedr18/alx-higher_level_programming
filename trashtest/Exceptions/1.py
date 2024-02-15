while True:
	try:
		x= int(input("Please Enter a valid integer: "))
		break
	except ValueError:
		print("Oops Please enter a valid integer!")
print(f"The value you entered is: {x}")