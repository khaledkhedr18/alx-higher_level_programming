"""Defines a square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Represent square """

    def __init__(self, size, x=0, y= 0, id= None):
        super().__init__(size, size, x, y, id)
	
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("length must be  0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        dic = {"id": self.id, "size": self.size,
               "x": self.x, "y": self.y}
        return dic

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.size}"

