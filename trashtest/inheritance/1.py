class Creature:
	def __init__(self, birthType="Unkown", appearance="Unkown", Bloods="Unknown"):

		self.appearance = appearance
		self.birth = birthType
		self.blood = Bloods

		@property
		def birthtype(self):
			return self.birthType
		


class Human(Creature):
	pass