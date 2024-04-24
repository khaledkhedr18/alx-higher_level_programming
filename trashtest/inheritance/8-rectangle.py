BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
	"""Represent a rectangle using BaseGeometry."""
	
	def __init__(self, width, height):
		self.integet_validator("width", width)
		self.__width = width
		self.integet_validator("height", height)
		self.__height = height