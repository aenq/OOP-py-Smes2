class Polygon:
	def __init__(PolygonType):
		print()

class Segitiga(Polygon):
	def __init__(self,setengah, alas,tinggi):
		self.setengah = setengah
		self.alas = alas
		self.tinggi = tinggi

	def luas(self):
		return self.setengah * self.alas * self.tinggi

class Segilima(Polygon):
	def __init__(self, lima, sisi):
		self.lima = lima
		self.sisi = sisi

	def keliling(self):
		return self.lima *self.sisi


Segitiga = Segitiga(1/2,5,10)
print("Luas Segitiga adalah ", Segitiga.luas())

Segilima = Segilima(5,20)
print("Keliling Segilima adalah", Segilima.keliling())