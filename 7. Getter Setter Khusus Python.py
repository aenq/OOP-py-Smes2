class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		#self.__name = name
		self.__health = health
		self.__armor = armor
		self.__info = "name :{}  \n\t health : {}".format(self.name, self.__health, self.__armor)

	@property
	def info(self):
		return "name :{}  \n\t health : {}".format(self.name, self.__health, self.__armor)
		#return self.__info #boleh make return yang ini juga

	@property
	def armor(self):
		pass

	@armor.getter
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self, input):
		self.__armor = input

	@armor.deleter
	def armor(self):
		self.__armor = None

sniper = Hero("sniper", 100, 10)

print("Merubah info")
#sebelum diubah
print("###sebelum")
print(sniper.info)

#setelah diubah
print()
print("###sesudah")
sniper.name = "dadang"
print(sniper.info)

print()
print("getter dan setter untuk __armor:")
print(sniper.armor) #akan none karena property armor masing "pass"
print(sniper.__dict__)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)
#armor nya akan berubah

print()
print("Delete armor")
del sniper.armor
print(sniper.armor)
print(sniper.__dict__)