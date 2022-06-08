class Buku:
	def __init__(self, judul, pengarang, jumlah_halaman):
		self.judul = judul
		self.pengarang = pengarang
		self.jumlah_halaman = jumlah_halaman

	def ShowInfo(self):
		print("Judul Buku 		:", self.judul)
		print("Pengarang 		:", self.pengarang)
		print("Jumlah Halaman 	:", self.jumlah_halaman)

class Novel(Buku):
	def __init__(self, judul, pengarang, jumlah_halaman):
		self.judul = judul
		self.pengarang = pengarang
		self.jumlah_halaman = jumlah_halaman
		print()
		super().ShowInfo()
		print("Tipe Buku 		: Novel")

class Majalah(Buku):
	def __init__(self, judul, pengarang, jumlah_halaman):
		self.judul = judul
		self.pengarang = pengarang
		self.jumlah_halaman = jumlah_halaman
		print()
		super().ShowInfo()
		print("Tipe Buku 		: Majalah")

class Buku_Pelajaran(Buku):
	def __init__(self,  judul, pengarang, jumlah_halaman):
		self.judul = judul
		self.pengarang = pengarang
		self.jumlah_halaman = jumlah_halaman
		print()
		super().ShowInfo()
		print("Tipe Buku 		: Buku Pelajaran")

Dilan = Novel("Dilan 1990", "Pidi Baiq", 400)
Bobo = Majalah("Bobo", "Kurang tau", 30)
IPA = Buku_Pelajaran("Mari Belajar IPA", "Siti", 300)

