class Person:
	def __init__(self, name):
		self.name = name
	def say_hello(self):
		print("Hi, my name is", self.name)

p = Person('khaled')
p.say_hello()