class Hero:

	def __init__(self, name, health, attackpower):
		#kita buat private dulu gaes
		self.__name = name
		self.__health = health
		self.__attackpower = attackpower

	#getter
	def getName(self):
		return self.__name

	def getHealth(self):
		return self.__health

	#setter
	def diserang(self, serangpower):
		self.__health -= serangpower

# awal dari game
earthshaker = Hero("Earth Shaker", 50, 5)

# game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())