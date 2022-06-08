import math

class bangunRuang(object):
	"""docstring for bangunRuang"""
	def __init__(self,nama):
		self.nama = nama
		self.luas = None
		self.tinggi = None
		print("Nama bangun ini adalah {}".format(self.nama))

	def volume(self):
		self.luas = int(input("Luas :"))
		self.tinggi = int(input("Tinggi :"))
		self.volume = self.luas*self.tinggi
		return self.volume

print("NOMOR 1")
print()
bangun1 = bangunRuang("Bangun1")
print("Volume bangun ruang tersebut adalah:",bangun1.volume())

class Tabung(bangunRuang):
	def __init__(self):
		super().__init__("Tabung")

	def volume(self):
		self.jarijari = int(input("Jari jari :"))
		self.tinggi = int(input("Tinggi:"))
		self.volume = math.pi * (self.jarijari**2) * self.tinggi
		print("Volume {} adalah {}".format(self.nama,self.volume))

class Balok(bangunRuang):
	def __init__(self):
		super().__init__("Balok")

	def volume(self):
		self.panjang = int(input("Panjang :"))
		self.lebar = int(input("Lebar :"))
		self.tinggi = int(input("Tinggi :"))
		self.volume = self.panjang*self.lebar*self.tinggi
		print("Volume {} adalah {}".format(self.nama,self.volume))

class Bola(bangunRuang):
	def __init__(self):
		super().__init__("Bola")

	def volume(self):
		self.jarijari = int(input("Jari-jari :"))
		self.volume = 4/3 * math.pi * (self.jarijari**3)
		print("Volume {} adalah {}".format(self.nama,self.volume))

print()
print("NOMOR 2")
print()
tabung1 = Tabung()
tabung1.volume

print()
balok1 = Balok()
balok1.volume()

print()
bola1 = Bola()
bola1.volume()


