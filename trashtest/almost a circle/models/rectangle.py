""" Defines a rectangle class """
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""
	
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width of this rectangle """
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__y = value
    
    def area(self):
        """ Returns the are of the rectangle. """
        return (self.__width * self.__height)

    def display(self):
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for i in range(self.__x):
                print(" ", end = "")
            for i in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """ This function updates the values of object rectangle """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]



    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")