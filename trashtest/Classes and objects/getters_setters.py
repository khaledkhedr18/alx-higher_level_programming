class Robot:
	def __init__ (self, name = None, build_year = None):
		self.name = name
		self.build_year = build_year

	def say_hi(self):
		if self.name:
			print("Hi, i am " + self.name)
		else:
			print("Hi, i am a robot without a name")
		if self.build_year:
			print("I was built in " + self.build_year)
		else:
			print("I am not built yet")

	def set_name(self, name):
		self.name = name
	def get_name(self):
		return self.name
	def set_build_year(self, by):
		self.build_year = by
	def get_build_year(self):
		return self.build_year
	
x = Robot()
x.set_name("Khaled")
x.set_build_year("2006")
x.say_hi()

y = Robot()
y.set_name(x.get_name())
print(y.get_name())