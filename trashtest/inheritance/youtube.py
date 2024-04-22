class Animal:
	def __init__(self, birthType="unknown", appearance="unknown", blooded="unknown"):
		self.birth = birthType
		self.appearance = appearance
		self.blooded = blooded

	@property
	def birthType(self):
		return self.__birthType
	
	@birthType.setter
	def birthType(self, birthType):
		self.__birthType = birthType


	@property
	def blooded(self):
		return self.__blooded
	
	@birthType.setter
	def blooded(self, blooded): 
		self.__blooded = blooded


	@property
	def appearance(self):
		return self.__appearance
	
	@appearance.setter
	def appearance(self, appearance):
		self.__appearance = appearance

		