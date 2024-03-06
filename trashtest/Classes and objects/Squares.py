class Square:
	def __init__(self, height = 0, width = 0):
		self.height = height
		self.width = width

	def set_height(self, height):
		if height.isdigit():
			print("Setting height")
			self.height = height
		else:
			print("Please enter a digit!")

	def set_width(self, width):
		if width.isdigit():
			print("Setting width")
			self.width = width
		else:
			print("Please enter a digit!")

	def get_height(self):
		return self.height
	
	def get_width(self):
		return self.width
	
	def getArea(self):
		print("Getting Area")
		return int(self.width) * int(self.height)
	


aSquare = Square()

height = input("Enter the height: ")
width = input("Enter the width: ")

aSquare.set_height(height)

aSquare.set_width(width)

print("Height: {}".format(aSquare.get_height()))
print("Width: {}".format(aSquare.get_width()))
print("Area: {}".format(aSquare.getArea()))