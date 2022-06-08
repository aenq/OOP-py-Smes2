class Hero:

 	def __init__(self, name, health):
 		self.name = name
 		self.health = health

 	def showInfo(self):
 		#print("{} \n\t Tipe: {},\n\t Health: {}".format(self.name, tipe, self.health))
 		print("{} \n\t Health: {}".format(self.name, self.health))

class Hero_intelligent(Hero):
	def __init__(self,name):
		super().__init__(name,100)
		

	# override
	def showInfo(self):
		print("Ini adalah show info di subclass intelligent")
		print("{} \n\t Tipe  : intelligent, \n\t Health:{}".format(
			self.name,
			self.health))

class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name, 300)

lina = Hero_intelligent("Lina")
lina.showInfo()
axe = Hero_strength("axe")
axe.showInfo()
