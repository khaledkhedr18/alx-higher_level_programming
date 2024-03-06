import random
import math

class Warrior:
	def __init__(self, name = "", health = 0, ad = 0, block = 0):
		self.name = name
		self.health = health
		self.ad = ad
		self.block = block

	def attack(self):
		attkamt = self.ad * (random.random() + 0.5)
		return attkamt
	def blockMax(self):
		blockamt = self.block * (random.random() + 0.5)
		return blockamt
	

class Battle:
	def startFight(self, warrior1, warrior2):
		Turn = 1
		while True:
			print("Round {}".format(Turn))
			if self.attackResult(warrior1, warrior2) == "Game Over":
				print("Game Over")
				break
			if self.attackResult(warrior2, warrior1) == "Game Over":
				print("Game Over")
				break
			Turn += 1
	@staticmethod
	def attackResult(warriorA, warriorB):
		warriorA_attackamt = warriorA.attack()
		
		warriorB_blockamt = warriorB.blockMax()

		dmg2warriorB = math.ceil(warriorA_attackamt - warriorB_blockamt)
		warriorB.health = warriorB.health - dmg2warriorB
	
		print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, dmg2warriorB))
		print(f"{warriorB.name} is down to {warriorB.health} health.")
		print()


		if warriorB.health <= 0:
			print(f"{warriorB.name} has died and {warriorA.name} is Victorious")
			return "Game Over"

		elif warriorA.health <= 0:
			print(f"{warriorA.name} has died and {warriorB.name} is Victorious")
			return "Game Over"
			
		else:
			return "Fight Continues"

	
def main():
	maximus = Warrior("Maximus", 50, 45, 10)

	achilles = Warrior("Achilles", 100, 20, 30)

	battle = Battle()

	battle.startFight(maximus, achilles)

main()