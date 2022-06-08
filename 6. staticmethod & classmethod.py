class Hero:
	# private class variable
	__jumlah = 0;

	def __init__(self, name):
		self.__name = name
		Hero.__jumlah += 1

	def getName(self):
		return self.__name

	# method ini hanya berlaku untuk object
	def getJumlah(self):
		return Hero.__jumlah

	# method ini tidak berlaku untuk object karna ga ada self
	# tapi berlaku untuk class
	def getJumlah1():
		return Hero.__jumlah

	# method static (decorator)
	@staticmethod
	def getJumlah2():
		return Hero.__jumlah

	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah

sniper = Hero("Sniper")
# kalo kita akses jumlah hero pasti gabisa karna private
# print(Hero.__jumlah) # akan error
# print(sniper.getJumlah()) 
print(Hero.getJumlah1())
print(sniper.getJumlah2())
rikimaru = Hero("Rikimaru")
print(rikimaru.getJumlah2())
drowranger = Hero("Drowranger")
print(drowranger.getJumlah2())

#coba class method
print(Hero.getJumlah3())
print(sniper.getJumlah3())
print(rikimaru.getJumlah3())
# jadi bedanya static dan classmethod itu, kalo class bisa ambil argumen 


# coba coba ajah bebas gaez
