class Hero:
	
	# class variabel
	jumlah = 0

	def __init__(self, name, health):
		self.name = name
		self.health = health

		# variable instance private
		self.__ayanaon = "private"
		# variable instance protected
		self._protected = "protected"

lina = Hero("Lina", 100)

print(lina.__dict__)
# print(lina.__ayanaon) # kalo diprint bakal error
print(lina._protected) # sama kayak public
print(lina.health)