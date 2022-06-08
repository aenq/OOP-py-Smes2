import math

class bangunRuang(object):
	"""docstring for bangunRuang"""
	def __init__(self,nama):
		self.nama = nama
		self.luas = None
		self.tinggi = None
		print("Nama bangun ini adalah {}".format(self.nama))

	def volume(self, luas, tinggi):
		self.volume = luas*tinggi
		return self.volume

print("NOMOR 1")
print()
bangun1 = bangunRuang("Bangun1")
print("Volume bangun ruang tersebut adalah:",bangun1.volume(25,10))

class Tabung(bangunRuang):
	def __init__(self):
		super().__init__("Tabung")

	def volume(self, r, tinggi):
		self.volume = math.pi * (r*2) * tinggi
		print("Volume {} adalah {}".format(self.nama,self.volume))

class Balok(bangunRuang):
	def __init__(self):
		super().__init__("Balok")

	def volume(self, panjang, lebar, tinggi):
		self.volume = panjang*lebar*tinggi
		print("Volume {} adalah {}".format(self.nama,self.volume))

class Bola(bangunRuang):
	def __init__(self):
		super().__init__("Bola")

	def volume(self,jarijari):
		self.volume = 4/3 * math.pi * (jarijari*jarijari*jarijari)
		print("Volume {} adalah {}".format(self.nama,self.volume))

print()
print("NOMOR 2")
print()
tabung1 = Tabung()
tabung1.volume(10,10)
print()
balok1 = Balok()
balok1.volume(10,6,15)
print()
bola1 = Bola()
bola1.volume(5)