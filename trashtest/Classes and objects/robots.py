class Robot:
	population = 0
	def __init__(self, name):
		self.name = name
		print(f"Initializing Robot {name}")

		Robot.population += 1

	def die(self):
		print(f"robot {self.name} is being destroyed")
		Robot.population -= 1 

		if Robot.population == 0:
			print(f"{self.name} was the last one")

		else:
			print(f"There are still {Robot.population:d} remaining")

	def say_hi(self):
		print(f"Greetings, my masters call me {self.name}")

	@classmethod
	def how_many(cls):
		print(f"we have {cls.population:d} robots")

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do work here")
print("Robots finished their work. Destroy!\n")

droid1.die()
droid2.die()

Robot.how_many()