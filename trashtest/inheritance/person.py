class Person(object):
	def __init__(self, name, id):
		self.name = name
		self.id = id

	def Display(self):
			print(self.name, self.id)

class Emp(Person):
	def __init__(self, name, id, salary, post):
		self.salary = salary
		self.post = post
		Person.__init__(self, name,id)

	def print(self):
		print("Emp class called")


emp = Person("satyam", 102)
emp.Display()
Emp_details = Emp("Mayank", 103)
Emp_details.Display()
Emp_details.print()