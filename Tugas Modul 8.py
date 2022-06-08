from abc import ABC, abstractmethod 
import math

class bangunDatar(ABC):
	def __init__(self, panjang, lebar):
		self.panjang = panjang
		self.lebar = lebar

class persegipanjang(bangunDatar):
	def luas(self):
		return self.panjang * self.lebar

	def keliling(self):
		return 2 * (self.panjang * self.lebar)

class segitigasiku(bangunDatar):
	def __init__(self, alas, tinggi):
		self.alas = alas
		self.tinggi = tinggi

	def luas(self):
		return (self.alas * self.tinggi)/2

	def keliling(self):
		sisimiring = math.sqrt(self.alas**2 + self.tinggi**2)
		return self.alas + self.tinggi + sisimiring

pp = persegipanjang(20,10)
print("Luas Persegi Panjang adalah", pp.luas(), "CM")
print("Keliling Persegi Panjang adalah", pp.keliling(), "CM")

print()

segitigasiku = segitigasiku(10, 10)
print("Luas Segitiga Siku adalah", segitigasiku.luas(), "CM")
print("Keliling Segitiga Siku adalah", segitigasiku.keliling(), "CM")