class Hero:

 	def __init__(self, name, health):
 		self.name = name
 		self.health = health

 	def showInfo(self):
 		print("{} dengan health {}".format(self.name, self.health))

class Hero_intelligent(Hero):
	def __init__(self,name):
		"""self.name = name
		   self.health = 100 """
		super().__init__(name,100)
		super().showInfo()

class Hero_strength(Hero):
	def __init__(self,name):
		"""self.name = name
		   self.health = 300"""
		super().__init__(name, 300)
		super().showInfo()
		# Hero.showInfo(self)

lina = Hero_intelligent("Lina")
axe = Hero_strength("axe")
rachel = Hero_intelligent("rachel")

print(lina.name , " " , lina.health)
print(axe.name , "  " , axe.health)
