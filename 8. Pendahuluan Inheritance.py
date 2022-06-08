 class Hero:

 	def __init__(self, name, health, landmother):
 		self.name = name
 		self.health = health
 		self.landmother = landmother

class Hero_intelligent(Hero):
	pass

class Hero_strength(Hero):
	pass

lina = Hero("Lina",100, "jakarta")
techies = Hero_intelligent("techies", 50, "bogor")
rachel = Hero_strength("rachel", 700, "madinah")

print(lina.name)
print(techies.health)
print(techies.landmother)
print(rachel.landmother)