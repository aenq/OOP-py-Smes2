class Hero: #template
	# class variable
	jumlah = 0

	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		#Instance Variable
		self.name = inputName		
		self.health = inputHealth
		self.power = inputPower
		self.Armor = inputArmor
		Hero.jumlah += 1
		print("membuat Hero dengan nama :", inputName)

hero1 = Hero("Sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("Rachel", 1000, 100, 9)
print(Hero.jumlah)

print(hero1.__dict__)