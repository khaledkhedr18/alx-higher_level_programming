class Creature:
	def __init__(self, name, species, blood):
		self.name = name
		self.species = species
		self.blood = blood

	@property
	def birthtype(self):
		return self.birthtype

class Human(Creature):
	pass